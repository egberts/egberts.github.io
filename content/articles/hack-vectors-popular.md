title: Popular Hack Vectors on Windows
Date: 2016-04-03 01:14
tags: hack, vector, methods
category: research
status: draft
slug: hack-vectors-popular

Most Popular Attacks
====================

In 2001, checksums were useful enough to confuse the reverse engineers of
network protocols.

Nowadays, PBKs with fancy debuggers are the greatest adversaries. Such fancy
debuggers are but not limited to:

* IDA Pro
* IDA Pro with HexRay
* OllyDbg
* WinDbg
* Cheat Engines
* Hopper
* Radare2

Some of the popular attack vector on Windows are:
* Protocols (openssl.dll, Win32 API TLS calls)
* Data: Windows WM_GETTEXT
* Code: FLIRT, encrypted machine code
* Dumping + Debugging: encrypted code and data
* Custom Loader + IDA: really-encrypted code and data
* Debugging+patching: disabling protection (mausy31)[https://www.youtube.com/watch?v=mOUPOkJoseE]
* Backtracing stack - this is where system calls cannot hide and who is calling these system calls
* Debugging+data-analysis: RTTI, VMT pointer (Sabanal Yason)[https://www.blackhat.com/presentations/bh-dc-07/Sabanal_Yason/Paper/bh-dc-07-Sabanal_Yason-WP.pdf]
* host-based Man-in-the-Middle (MITM)
* Hooks (Aiko)[https://www.blackhat.com/presentations/bh-jp-08/bh-jp-08-Aiko/bh-jp-08-Aiko-EN.pdf]

        Protocol-level: Self-MITM
        Hooks (see, for example, [Aiko])

