Title: SSH Overview
Date: 2016-09-24T12:08
Tags: ssh
Category: research
This page details the hardening of SSH.

* [SSH client](SSH_client "wikilink")
* [SSH server](SSH_server "wikilink")

Algorithms Used
===============

To display available algorithms for a specific SSH client

```bash
ssh -Q cipher
ssh -Q cipher-auth
ssh -Q mac
ssh -Q kex
ssh -Q key
```

Audit
=====

Auto-Assess
-----------

To audit in a passive manner the SSH servers and clients, execute
`ssh-audit`.

`ssh-audit` (written in Python) can be found over at
[GitHub](https://github.com/jtesta/ssh-audit).

Manual Remediation
------------------

To manually check and ensure that the SSH is clamped down securely,
execute the following:

* <https://benchmarks.cisecurity.org/tools2/linux/CIS_Debian_Linux_8_Benchmark_v1.0.0.pdf>
* <https://benchmarks.cisecurity.org/tools2/linux/CIS_Debian_Linux_7_Benchmark_v1.0.0.pdf>

Make effective all changes, by executing:

```bash
    systemctl reload sshd.service
```

Escape Codes
============

Did you know that when you’re using OpenSSH from the command line you
have a variety of escape sequences available to you? SSH somewhere, then
type “~” and “?” (tilde, then question mark) to see all the options. You
should get something like: SSH Escape Codes

Supported escape sequences:

[jtable]
command sequence, description
~., connection (and any multiplexed sessions)
~B, a BREAK to the remote system
~C, a command line
~R, rekey (SSH protocol 2 only)
~^Z, ssh
~#, forwarded connections
~&, ssh (when waiting for connections to terminate)
~?, message
~~, the escape character by typing it twice

Most commonly, I use tilde-period (~.) to close an unresponsive session,
like when a firewall has closed my connection. BREAK is useful for
various things, usually getting back to a terminal server console or
getting the attention of network equipment. The command line doesn’t do
much, but you can alter forwards from it. I’ve never used it but it’s
probably handy for troubleshooting if your tunnels aren’t working right:

```ssh
ssh> ?
Commands:`
     -L[bind_address:]port:host:hostport
     -R[bind_address:]port:host:hostport
     -D[bind_address:]port
     -KR[bind_address:]port
```

Request local forward Request remote forward Request dynamic forward
Cancel remote forward

I’ve also never had to rekey a session for any reason, as SSH protocol
version 2 does it automatically after a certain amount of data has been
transferred. You can mess with it via the RekeyLimit configuration
directives, or read more about it in RFC 4344. Suspending SSH via
tilde-Ctrl-Z is handy from time to time, especially when you’re on the
console of a machine that doesn’t have screen or some other multiplexer
on it (or you forgot to start one). Of course, you have to remember that
when you need it, but now that you’ve read it maybe you will.

List forwarded connections is handy for managing the forwards you might
have created with the command line. Backgrounding SSH attempts to close
all the connections, and will wait patiently for them to die. I have
never needed this, because I’m the impatient bastard that just
tilde-periods them if they don’t close right away.

You can use the EscapeChar configuration directive to change the tilde,
if that conflicts with something. Or you can just type it twice to send
it.
