Title: Bind9 Keys
Date: 2018-11-13 12:54
Tags: DNSSEC, dns, bind9
Category: research
slug: bind9-keys
summary: Keys Used in DNSSEC

DNS Keys

There are several types of crypto keys used by DNS and Bind9.

* TSIG
* DDNS
* RNDC
* GSS

You can use RFC 2136 "DNS UPDATE", either by scripting the nsupdate tool
or by using a compatible third-party client: Shared secret key (TSIG)

To generate a secret key for authenticating the DNS record updates:

```shell
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

```shell
  zone … {
      …
      update-policy {
          /* grant `<key_name>` `<policy>` `<record_types>` */
          grant "tsig-key" name myserver.example.com ANY;
      };
  };
```
Various different policies can be used; e.g. zonesub allows updating the
entire zone, and subdomain dyn.example.com has the obvious meaning.

To perform DNS record updates:

```shell
  $ nsupdate -k tsig-key.private
  > zone example.com
  > del myserver.example.com
  > add myserver.example.com 3600 A 100.64.1.1
  > send
```

There are various clients capable of automatic updates. Public/private
key (SIG(0))

To enerate a public/private key pair:

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
not need to match the hostname you're updating, though.) Kerberos
(GSS-TSIG)

A bit out of scope, but BIND9 supports this as well (mainly for use with
Active Directory).
