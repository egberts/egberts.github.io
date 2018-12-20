Title: Custom Home Router, Verizon
date: 2018-11-10T14:18
modified:  2018-11-13T12:55
tags: verizon, router, homelan
category: research

Ethernet via ONT
================

Your throughput is a bit higher using that Ethernet port on the ONT than
letting an Verizon-provided broadband modem router bridge the MoAC cable
into providing that Ethernet.

* ActionTec Rev A/C/D MoCa has 100 Mbps throughput
* ActionTec Rev E/F MoCa has 100 Mbps throughput
* ActionTec Rev. G/I MoCA has 175 Mbps throughput
* FiOS Quantum Gateway MoCA has 200 Mbps throughput

whereas:

* ONT direct Ethernet goes up to 1 Gbps throughput

So just for Internet/data service, why bother with MoCA or R6 cabling?

Call Verizon Support, ask to "bridge the Ethernet at the ONT" using the
same Verizon's own router but through Ethernet (instead of RG-6) cable.
Be patient. Escalate to level 2 if necessary.

Clone MAC address
-----------------

If you plan to keep the Verizon-provided modem router because of Cable
TV, then you will have to clone the MAC address.

If you are strictly an Internet-only household, then no need to clone
MAC address of Verizon-provided router because you can return it and
save $12/month.

I used to recommend cloning the MAC address of your FiOS router onto
your new router. However, one commenter had a pretty terrible time with
this, and actually had his service cancelled. Instead, I recommend using
your router with it’s true MAC address. This will most likey involve a
call to Verizon, but it’s worth a few minutes on the phone.

As for me, I've successfully cloned the MAC address ONLY because I use
custom ISC DHCP client that mirrored the behavior of the original
ActionTec broadband modem router. I can clone MAC only because I am
still holding the ActionTec equipment.

References
==========

* <https://loganmarchione.com/2015/07/use-your-own-router-with-verizon-fios/#comment-152266>

