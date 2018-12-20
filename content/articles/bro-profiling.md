Title: Profiling Bro
Date: 2018-09-24 09:33
Tags: Bro, profiling
Slug: bro-profiling
category: research
summary: How to run OProfile on Bro IDS

Profiling Bro
=============

This page describes how to run OProfile Get two packages from
<http://debuginfo.centos.org/6/x86_64/>

* kernel-debuginfo-x86\_64-\`uname -r\`.rpm
* kernel-debuginfo-common-x86\_64-\`uname -r\`.rpm
* oprofile

Set up the kernel
-----------------

```bash
opcontrol --setup --vmlinux=/usr/lib/debug/lib/modules/`uname -r`/vmlinux`
# if no vmlinux available, execute
opcontrol --setup --no-vmlinux
```

Note: vmlinux must be UNSTRIPPED (HAVE symbols) in its ELF2 file.
Extracting from /boot/vmlinuz-... will not work.

Configure Kernel to run oprofile:

```bash
echo 0 > /proc/sys/kernel/nmi_watchdog
#  and collect
opcontrol --reset
opcontrol --separate=lib,kernel
opcontrol --start
# run your app(s)
opcontrol --deinit
opreport
```

Example Reports
===============

The oprofile reports are largely shaped by the granularity of statistics
collection in the following groups:

*CPUs
*Threads
*NUMAs

