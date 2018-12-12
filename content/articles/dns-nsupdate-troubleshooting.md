Title: nsupdate Troubleshooting
Date: 2018-10-17T20:50
Status: published
Tags: nsupdate, dns, troubleshooting
Category: research
nsupdate

Protocol/Port
=============

Network port/protocol used: 53/udp or 53/tcp (using `-v` option)

Note: `rndc` uses:

* 953/udp with any key-file (defaults to `rndc-key`, or
* named-generated file-based key in `/var/lib/bind/session.key`.

nsupdate commands
=================

server
------

Using \`server server-ip\` will perform the following with unexpected
result (if you are doing esoteric network topology):

* a query lookup of SOA on that server-ip,
* extract the MNAME field from the SOA record, and
* then only interact with that MNAME server.

This is different from \`local server-ip\` or \`nsupdate -l\`.

Keys used
=========

You can use RFC 2136 "DNS UPDATE", either by scripting the nsupdate tool
or by using a compatible third-party client:

Shared secret key (TSIG)
------------------------

Generate a secret key for authenticating the updates:

```bash
   $ tsig-keygen -r /dev/urandom | tee tsig-key.private
   key "tsig-key" {
       algorithm hmac-sha256;
       secret "7P6HbRZRJCmtauo/lV0jwN9wkMgBTUikhf9JuaTvYT4=";
   };
```

This key is known to the server and client, and nobody else.

Copy the printed text into your named.conf. (You can have multiple keys
for different hosts, each with a unique name in the key "…" field.)

Enable dynamic updates in the zone configuration:

```bind
   zone … {
       …
       update-policy {
           /* grant <key_name> <policy> <record_types>` */
           grant "tsig-key" name myserver.example.com ANY;
       };
   };
```

Various different policies can be used; e.g. zonesub allows updating the
entire zone, and subdomain dyn.example.com has the obvious meaning.

Perform updates:

```shell
$ nsupdate -k tsig-key.private
> zone example.com
> del myserver.example.com
> add myserver.example.com 3600 A 100.64.1.1
> send
```

There are various clients capable of automatic updates.

Public/private key (SIG(0))
---------------------------

Generate a key pair:

```shell
$ dnssec-keygen -r /dev/urandom -T KEY -n USER myclient.example.com
$ ls K*
Kmyclient.example.com.+005+07399.key
Kmyclient.example.com.+005+07399.private
```

The \*.key file contains the public key – add it to your DNS zone.

The \*.private file contains the private key – copy it to the client
computer. (Actually, copy both files to the client computer.)

Set up update-policy { } in exactly the same way as with TSIG.

Perform updates also in the same way using nsupdate -k
<filename>.private.

(Note: While TSIG key names are arbitrary, SIG(0) keys are stored in DNS
and therefore always named like hostnames/subdomains. The key name does
not need to match the hostname you're updating, though.)

Kerberos (GSS-TSIG)
-------------------

A bit out of scope, but BIND9 supports this as well (mainly for use with
Active Directory).

Troubleshooting
===============

nsupdate updating other nameserver
----------------------------------

Might want to check that you are using \`local server-ip\` and not
\`server server-ip\` command.

Using \`server server-ip\` will perform the following with unexpected
result (if you are doing esoteric network topology):

* a query lookup of SOA on that server-ip,
* extract the MNAME field from the SOA record, and
* then only interact with that MNAME server.

It can lead to disastrous result if you are using
hidden-master/public-slave or stealth master network topology.

Instead, do one of the following:

* Use \`local server-ip\` to minimize this impact or
* use \`nsupdate -l\` via \`/var/lib/bind/dynamic/session.key\` that got created during Bind config \`update-policy local\`.

update failed: NOTAUTH
----------------------

```bash
nsupdate -l -M
> zone example.net red
> update delete arca.example.net
> send`
update failed: NOTAUTH
```

You'll see in the packet that DNS Dynamic Update, follow by Dynamic
Update Response packet.

In the DNS Dynamic Update Response packet, Wireshark-expert mode
reported that there is no dissector for HMAC-SHA256.

Also

    0x1001 Reply Code: Not Authoritative (9)

update failed: NOTAUTH(BADKEY)
------------------------------

Check the /var/log/bind/security.log for:

```
security: error: client 127.0.0.1#25080: view gateway: request has invalid` signature: TSIG ddns-key.arca.example.net: tsig verify failure (BADKEY)
```

nsupdate can only handle hmac-md5. You probably used an algorithm other
than HMAC-MD5 (i.e. hmac-sha256)

For correct creation of ddns.conf is `ddns-confgen` `-a` `HMAC-MD5`.

Replace the key with a correct algorithm. Keys between BIND9 and ISC
DHCP must use `hmac-md5` as this is a ISC DHCP design limitation.

update failed: NOTAUTH(BADSIG)
------------------------------

This means that there is no signature ... at all ... to be found.
Perhaps its key name was misspelled. Perhaps it is missing.

No signing records found
------------------------

```bash
$ rndc signing -list example.net.
No signing records found
```

It means that there is no TEMPORARY RRDATA found in the example.net zone
file as reported by `ns_server_signing()` function in `named/server.c`.
This command is totally useless and is only practical when using against
very large zone file.
