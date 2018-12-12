Title: Comparison of Memory Allocation Methods
Date: 2017-10-20T12:53
Modified: 2018-07-07T20:42
Tags: comparison, malloc
Category: research
summary: A comparison of memory allocation libraries.

Memory Allocation
=================

Problems
--------

Limit Memory Allocation (if not necessary)

Multithreaded programs often do not scale because the heap is a
bottleneck.

When multiple threads simultaneously allocate or deallocate memory from
the allocator, the allocator will serialize them. Programs making
intensive use of the allocator actually slow down as the number of
processors increases.

Malloc (libc) is the worse memory allocation API to use.

Programs should avoid, if possible, allocating/deallocations memory too
often and in particular whenever a packet is received.

In the Linux kernel there are available kernel/driver patches for
recycling skbuff (kernel memory used to store incoming/outgoing
packets).

Using PF\_RING (into the driver) for copying packets from the NIC to the
circular buffer without any memory allocation increases the capture
performance (around 10%) and reduces congestion issues.

Design Evolution
================

Basic design of malloc() is to dynamically pre-allocate a pool of memory
from the OS in which applications can then take smaller pieces from.
malloc() is a standard API having a choice of different allocation
algorithms and to mitigate the expensive OS system calls (typically done
at program initialization time) during allocation of its system memory.
The first memory allocation scheme started with a stack-based memory
allocation.

Next came the dynamic-based memory allocation scheme where linked-list
and bucket-heap mechanism are used to divide the private-heap using size
class approach.

Soon, garbage collection algorithm introduced the initial backend of the
memory allocation scheme. Frontend covers the usual malloc() API, et.
al.

In 2006, a third pool was introduced (after operating system memory pool
and library-based memory pool) called the "arena". Arena is a
jemalloc-term and is intended to deal with different memory types such
as different-speed memory bank or NUMA-architecture, as well as memory
tied to specific to each of the multiple CPU core or even CPU infinity.

Frontend Evolution
------------------

Frontend manages the memory being given to the application.

Within the frontend of the memory allocation system, the evolution went
in the following order:

1. link-list free space
2. heap-bucket size classes (eliminating an object header)
3. (Process) Owner encoding
4. single core local allocation buffers (CLABs)
5. Epoch encoding
6. Large-size class memory block by direct mmap()
7. Hazard pointers (safe memory reclamation for lock-free objects) (M.M. Michael, 2004)
8. Arena memory pool
9. thread-specific local allocation buffers (TLABs)
10. constant-time modulo synchronization (early return to OS pool, or FreeBSD madvise call)

Backend Evolution
-----------------

Backend of the memory allocation system manages the empty, straggling,
fragmented or no-longer used memory blocks back to the OS (thereby
reducing RSS).

* Pool semantic: Remote f-list encoding, using Treiber stack), (R.K.
    Treiber,
* 1986)
* buddy algorithm
* binary buddy algorithm
* BIPOP Table (span-based allocator)(S. Schneider, 2006) aka local
    free list and
* remote free list
* segment queue (Quasi-linearizability, Y. Afek, 2010)
* multi-core distributed queue (A. Haas, 2013)
* k-FIFO queue (T.A. Henzinger, 2013)

Competition
-----------

There are better ones out there that does not worsen as more
threads/processes performs memory allocation system calls; they are
listed in best-to-good performance order​\[seed with source\]:

Comparison of malloc design
===========================

[jtable]
name , Author , link , repo
ssmalloc , , <a href="https://apsys2012.kaist.ac.kr/media/papers/apsys2012-final27.pdf">whitepaper</a>,
jemalloc , Jason Evans (Facebook, FreeBSD) , [whitepaper](https://people.freebsd.org/~jasone/jemalloc/bsdcan2006/jemalloc.pdf) , 
sfmalloc , "SNU, Korea" , , 
Streamflow , , , 
ptmalloc3 , , , 
nedmalloc-1.02 , , , 
lockless , , , 
ptmalloc2 , GNU Libc (dlmalloc-forked) , , 
Hoard , , , 
libumem , SMI Solaris , , 
mtmalloc , , , 
nedmalloc-1 , , , 
tcmalloc , Google , , 
ctmalloc , Google Code , , 
ptmalloc , GNU Libc (dlmalloc-forked) , , 
dlmalloc , "Doug Lea, FreeBSD" , <a href="http://g.oswego.edu/dl/html/malloc.html">blog</a>, <a href="ftp://g.oswego.edu/pub/misc/malloc.c">FTP</a>
pkmalloc , , <a href="http://www.freebsd.dk/pubs/malloc.pdf">whitepaper</a>, 
phkmalloc , FreeBSD , , 
malloc , GNU Libc (glibc) , ,
[/jtable]

Features of malloc
------------------

Algorithms - best-first

* Wilderness Preservation - The \`\`wilderness'' chunk represents the space bordering the topmost address allocated from the system. Because it is at the border, it is the only chunk that can be arbitrarily extended (via sbrk in Unix) to be bigger than it is
* Deferred Coalescing - Rather than coalescing freed chunks, leave them at their current sizes in hopes that another request for the same size will come along soon. This saves a coalesce, a later split, and the time it would take to find a non-exactly-matching chunk to split.
* Preallocation - Rather than splitting out new chunks one-by one, pre-split many at once. This is normally faster than doing it one-at-a-time.

[jtable]
name, Algorithm, Wilderness Preservation, Deferred coalescing free chunk, Pre-split free chunk
ssmalloc ,,,,
jemalloc ,,,,
sfmalloc ,,,,
Streamflow ,,,,
ptmalloc3 ,,,,
nedmalloc-1.02 ,,,,
lockless ,,,,
ptmalloc2 ,,,,
Hoard ,,,,
libumem ,,,,
mtmalloc ,,,,
nedmalloc-1 ,,,,
tcmalloc ,,,,
ctmalloc ,,,,
ptmalloc ,,,,
dlmalloc , best-first , Y , Y , Y 
pkmalloc ,,,,
phkmalloc ,,,,
malloc ,,,,
[/jtable]

Unit Test Approaches
====================

Malloc testing

Test various patterns of memory allocation, aiming for various levels of
fragmentation. Perform the tests both in single-threaded and
multi-threaded environments.

Checks for correctness:

* None of the allocated blocks should overlap, and all should be successfully writable for the requested number of bytes.
* Allocations made by posix\_memalign should be correctly aligned and freeable by free.
* Arguments to calloc which would overflow size\_t when multiplied should result in allocation failure, not under-allocation.
* Allocating a block so large that subtracting two pointers within that block could overflow ptrdiff\_t should not be possible.

Further implementation-specific correctness checks: checking consistency
of bookkeeping information before and after each allocated block.

Possible quality-of-implementation checks: Attempting to obtain
pathological fragmentation and allocation failure where it should not
happen.

Corruption check: The attacker could overflow a buffer dynamically
allocated by malloc(3) and:

* overwrite the next contiguous boundary tag ([Netscape browsers exploit](<http://www.openwall.com/advisories/OW-002-netscape-jpeg.txt) or
* underflow such a buffer and overwrite the boundary tag stored just before [Secure Locate exploit](ftp://maxx.via.ecp.fr/dislocate/)), or
* cause the vulnerable program to perform an incorrect free(3) call [LBML traceroute exploit](http://www.synnergy.net/downloads/exploits/traceroute-exp.txt), or
* freeing [multiple frees](ftp://maxx.via.ecp.fr/traceroot/), or
* overwrite a single byte of a boundary tag with a NUL byte (Sudo exploit)

Known malloc exploits:

* [http://www.phrack.org/issues.html?issue=57&id=8#article]
* [https://sploitfun.wordpress.com/2015/03/04/heap-overflow-using-malloc-maleficarum/]
* [http://phrack.org/issues/66/10.html]

References
==========

* [https://sploitfun.wordpress.com/2015/02/10/understanding-glibc-malloc]
* Origin of the word malloc is [here](https://www.spinellis.gr/blog/20170914/).
* History of malloc is \[ here\].
* Heap and allocators
* [here](http://www.cs.dartmouth.edu/~sergey/cs108/2015/heaps-and-allocators.txt)
* [Anatomy of a Program in Memory](https://manybutfinite.com/post/anatomy-of-a-program-in-memory/)

