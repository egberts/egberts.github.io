Libpcap to capture 10Gbps
=========================

:Tags: pcap, libpcap, Ethernet, high-speed
:Date: 2014-12-14 20:34
:Status: published
:Category: research

Someone asked:

I want to capture packets from 10Gbps network card with 0 packet loss. I am
using lipcap for 100Mbps NIC and it is working fine. Will libpcap be able to
handle 10Gbps NIC traffic? If not what are the other alternative ways to achive
this?

I answered:

You don't say which Operating System or CPU. It doesn't matter whether you
choose libpcap or not, the underlying network performance is still burdened by
the Operating System Memory Management and its network driver. libpcap has kept
up with the paces and can handle 10Gbps, but there's more.

If you want the best CPU so that you can do number-crunching, running virtual
machines and while capturing packets, go with AMD Opteron CPU which still
outperforms Intel Xeon Quadcore 5540 2.53GHz (despite Intel's XIO/DDIO
introduction and mostly because of Intel dual-core sharing of same L2 cache).
For best ready-made OS, go with latest FreeBSD as-is (which still outperforms
Linux 3.10 networking using basic hardware.) Otherwise, Intel and Linux will
works just fine for basic drop-free 10Gbps capture, provided you are eager to
roll up your sleeves.

If you're pushing for breakneck speed all the time while doing financial-like or
stochastic or large matrix predictive computational crunching (or something),
then read-on...

As RedHat have
[discovered](people.netfilter.org/hawk/presentations/nfws2014/dp-accel-10G-challenge.pdf), 67.2 nanosecond is what it takes to process one
minimal-sized packet at 10Gbps rate. I assert it's closer to 81.6 nanosecond for
64 byte Ethernet payload but they are talking 46-byte minimal as a theoretical.

To cut it short, you WON'T be able to DO or USE any of the following if you want
0% packet drop at full-rate by staying under 81.6 ns for each packet:

* Make an SKB call for each packet (to minimize that overhead, amortized this over several 100s of packets)
* TLB (Translation lookaside buffer, to avoid that, use HUGE page allocations)
* Short latency (you did say 'capture', so latency is irrelevant here). It's called Interrupt Coalesce (`ethtool -C rx-frames 1024+`).
* Float processes across multi-CPU (must lock them down, one per network interface interrupt)
* libc `malloc()` (must replace it with a faster one, preferably HUGE-based one)

So, Linux has an edge over FreeBSD to capture the 10Gbps rate in 0% drop rate
AND run several virtual machines (and other overheads). Just that it requires a
new memory management (MM) of some sort for a specific network device and not
necessarily the whole operating system. Most new super-high-performance network
driver are now making devices use HUGE memory that were allocated at userland
then using driver calls to pass a bundle of packets at a time.

Many new network-driver having repurposed MM are out (in no particular order):

* netmap
* PF-RING
* PF-RING+netmap
* OpenOnload
* DPDK
* PacketShader

The maturity level of each code is highly dependent on which Linux (or distro)
version you choose. I've tried a few of them and once I understood the basic
design, it became apparent what I needed. YMMV.
