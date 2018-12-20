Title: Bro messaging
Date:  2018-05-16 14:16:28
Tags: Bro, API
Category: research
Summary: Enabling debug messages of Bro script
Debugging Bro message queues
============================

To enable debugging Bro message queues, insert the following into the
local.bro script in /usr/share/bro/sfa/policy directory. This is also
useful for troubleshooting script-land memory leakage.

```bro
@load misc/profiling
redef Log::enable_local_logging = T;
redef profiling_interval = 10secs;
redef expensive_profiling_multiple = 2;
```

Bro UNIX server created a prof.log file. As a UNIX server, prof.log are
found in each of the /var/spool/bro/***bro-process-type*** directory.
Running Bro as standalone puts prof.log in the current working
directory.

Example output of prof.log:

```
    0.000000 ------------------------
    0.000000 Command line: /usr/bin/bro -C -d -B threading -t trace.log -e redef
    profiling_interval=30secs;
    redef expensive_profiling_multiple=1 ; redef Log::enable_local_logging=T; redef
    Reporter::info_to_stderr =
    T; redef Reporter::errors_to_stderr = T; redef Reporter::warnings_to_stderr = T;
    -r ftp.pcap
    sfa/policy/local.bro
    0.000000 ------------------------
    0.000000 Memory: total=30160K total_adj=0K malloced: 23126K
    0.000000 Run-time: user+sys=0.0 user=0.0 sys=0.0 real=0.0
    0.000000 Conns: total=0 current=0/0 ext=0 mem=0K avg=-nan table=1K connvals=0K
    0.000000 Conns: tcp=0/0 udp=0/0 icmp=0/0
    0.000000 TCP-States:        Inact.  Syn.    SA      Part.   Est.    Fin.    Rst.
    0.000000 TCP-States:Inact.
    0.000000 TCP-States:Syn.
    0.000000 TCP-States:SA
    0.000000 TCP-States:Part.
    0.000000 TCP-States:Est.
    0.000000 TCP-States:Fin.
    0.000000 TCP-States:Rst.
    0.000000 Connections expired due to inactivity: 0
    0.000000 Total reassembler data: 0K
    0.000000 RuleMatcher: matchers=2 dfa_states=2 ncomputed=0 mem=2K
    avg_nfa_states=29
    0.000000 Timers: current=19 max=19 mem=1K lag=0.00s
    0.000000 DNS_Mgr: requests=0 succesful=0 failed=0 pending=0 cached_hosts=0
    cached_addrs=0
    0.000000 Triggers: total=0 pending=0
    0.000000
    0.000000
    0.000000
    0.000000 Threads: current=4
    0.000000   /var/spool/bro/bv_intel/bv_intel.txt/Input::READER_ASCII in=1 out=1
    pending=0/1 (#queue r/w:
    in=1/1 out=0/1)
    0.000000
    0.000000
    0.000000
    0.000000
    0.000000 Global_sizes > 100k: 0K
    ProfileTimer = 1
    ScheduleTimer = 2
    TableValTimer = 16
    packet_filter/Log::WRITER_ASCII in=1 out=0 pending=0/0 (#queue r/w: in=1/1
    out=0/0)
    packet_filter/Log::WRITER_ASCII in=1 out=0 pending=0/0 (#queue r/w: in=1/1
    out=0/0)
    loaded_scripts/Log::WRITER_ASCII in=1 out=0 pending=0/0 (#queue r/w: in=1/1
    out=0/0)
    reporter/Log::WRITER_ASCII in=1 out=0 pending=0/0 (#queue r/w: in=1/1 out=0/0)
    0.000000
    0.000000
    0.000000
    0.000000
    0.000000 Global_sizes total: 1173K
    0.000000 Total number of table entries: 1648/1691
    SSL::cipher_desc = 99K (351/351 entries)
    SSL::root_certs = 208K (147/147 entries)
    FTP::cmd_reply_code = 48K (325/325 entries)
    Weird::actions = 36K (162/162 entries)
```

Please note the (\#queue r/w: in=1/1 out=0/1) by
bv\_intel.txt/WRITER\_ASCII: this means one message was inserted into
the input queue and one message was removed from the same input queue,
while only one message was written to the output queue, but nobody has
retrieved it yet.

The prof.log output continues on (note the timestamp):

```
    1413471640.952530 ------------------------
    1413471640.952530 Memory: total=30160K total_adj=0K malloced: 23127K
    1413471640.952530 Run-time: user+sys=0.0 user=0.0 sys=0.0 real=0.0
    1413471640.952530 Conns: total=0 current=0/0 ext=0 mem=0K avg=-nan table=1K
    connvals=0K
    1413471640.952530 Conns: tcp=0/0 udp=0/0 icmp=0/0
    1413471640.952530 TCP-States:        Inact.  Syn.    SA      Part.   Est.
    Fin.    Rst.
    1413471640.952530 TCP-States:Inact.
    1413471640.952530 TCP-States:Syn.
    1413471640.952530 TCP-States:SA
    1413471640.952530 TCP-States:Part.
    1413471640.952530 TCP-States:Est.
    1413471640.952530 TCP-States:Est.
    1413471640.952530 TCP-States:Fin.
    1413471640.952530 TCP-States:Rst.
    1413471640.952530 Connections expired due to inactivity: 0
    1413471640.952530 Total reassembler data: 0K
    1413471640.952530 RuleMatcher: matchers=2 dfa_states=2 ncomputed=0 mem=2K
    avg_nfa_states=29
    1413471640.952530 Timers: current=18 max=19 mem=1K lag=1413471639.95s
    1413471640.952530 DNS_Mgr: requests=0 succesful=0 failed=0 pending=0
    cached_hosts=0 cached_addrs=0
    1413471640.952530 Triggers: total=0 pending=0
    1413471640.952530         ScheduleTimer = 2
    1413471640.952530         TableValTimer = 16
    1413471640.952530 Threads: current=4
    1413471640.952530   /var/spool/bro/bv_intel/bv_intel.txt/Input::READER_ASCII
    in=1 out=1 pending=0/0 (#queue
    r/w: in=1/1 out=1/1)
    1413471640.952530
    1413471640.952530
    1413471640.952530
    1413471640.952530 Global_sizes > 100k: 0K
    packet_filter/Log::WRITER_ASCII in=1 out=0 pending=0/0 (#queue r/w: in=1/1
    out=0/0)
    loaded_scripts/Log::WRITER_ASCII in=1 out=0 pending=0/0 (#queue r/w: in=1/1
    out=0/0)
    reporter/Log::WRITER_ASCII in=1 out=0 pending=0/0 (#queue r/w: in=1/1 out=0/0)
    1413471640.952530
    1413471640.952530
    1413471640.952530
    1413471640.952530
    1413471640.952530 Global_sizes total: 1173K
    1413471640.952530 Total number of table entries: 1648/1691
    1413471671.003551 ------------------------
    1413471671.003551 Memory: total=30160K total_adj=0K malloced: 23329K
    1413471671.003551 Run-time: user+sys=0.1 user=0.0 sys=0.0 real=0.1
    1413471671.003551 Conns: total=14 current=9/9 ext=0 mem=48488K avg=5387.6
    table=50K connvals=35K
    1413471671.003551 Conns: tcp=7/8 udp=2/6 icmp=0/0
    1413471671.003551 TCP-States:        Inact.  Syn.    SA      Part.   Est.
    Fin.    Rst.
    1413471671.003551 TCP-States:Inact.
    1413471671.003551 TCP-States:Syn.
    1413471671.003551 TCP-States:SA
    SSL::cipher_desc = 99K (351/351 entries)
    SSL::root_certs = 208K (147/147 entries)
    FTP::cmd_reply_code = 48K (325/325 entries)
    Weird::actions = 36K (162/162 entries)
    1413471671.003551 TCP-States:Part.
    1413471671.003551 TCP-States:Est.
    1413471671.003551 TCP-States:Fin.
    1413471671.003551 TCP-States:Rst.
    1413471671.003551 Connections expired due to inactivity: 0
    1413471671.003551 Total reassembler data: 0K
    1413471671.003551 RuleMatcher: matchers=2 dfa_states=40 ncomputed=150 mem=62K
    avg_nfa_states=1
    1413471671.003551 Timers: current=36 max=47 mem=2K lag=0.05s
    1413471671.003551 DNS_Mgr: requests=0 succesful=0 failed=0 pending=0
    cached_hosts=0 cached_addrs=0
    1413471671.003551 Triggers: total=0 pending=0
    1413471671.003551         ConnectionInactivityTimer = 11
    1413471671.003551         FileAnalysisInactivityTimer = 1
    ...
```

Analyzing prof.log
==================

Intel::data\_store size should remain unchanged during leakage/polling
periods. (Note: It is proportional to the size of bv\_intel.txt file.)

```
Global_sizes > 100k: 0K
               Communication::connected_peers = 2556K (18/18 entries)
               [FTP::cmd_reply_code](FTP::cmd_reply_code) = 48K (325/325 entries)
               Cluster::worker2manager_events = 155K
               Weird::actions = 37K (162/162 entries)
               Intel::min_data_store = 5386K
               Intel::data_store = 33904K
               SSL::cipher_desc = 101K (351/351 entries)
               Communication::nodes = 2588K (20/20 entries)
               SSL::root_certs = 209K (147/147 entries)
Global_sizes total: 45812K
```

Also Global\_sizes total should remain unchanged during all statistical
collection periods after initialization.

READER\_ASCII would not leak if it had a perfect one-to-one read/write
with input portion of Intel reader queue.

```
/var/spool/bro/bv_intel/bv_intel.txt/Input::READER_ASCII in=151 out=76527
pending=0/0 (\#queue r/w: in=151/151 out=76527/76527)

Total memory should be closely paid attention to for Bro Core Engine
leakage as it did in this 20-second example:

    Memory: total=32608K total_adj=0K malloced: 32478K
    ...
    Memory: total=123236K total_adj=90628K malloced: 78143K
    ...
    Memory: total=143088K total_adj=110480K malloced: 87989K
    ...
    Memory: total=164320K total_adj=131712K malloced: 108040K
    ...
    Memory: total=177040K total_adj=144432K malloced: 132104K
    ...
    Memory: total=177040K total_adj=144432K malloced: 133631K
    ...
    Memory: total=177040K total_adj=144432K malloced: 137221K
    ...
    Memory: total=177040K total_adj=144432K malloced: 139141K
```

Checkpointing of memory structures between Bro workers were less than 1K
every 20 seconds as denoted by this prof.log output:

```
    Conns: total=78555 current=1622/1622 ext=0 mem=0K avg=0.0 table=0K connvals=0K
    ...
    Conns: total=78555 current=1622/1622 ext=0 mem=0K avg=0.0 table=1K connvals=0K
    ...
    Conns: total=78555 current=1622/1622 ext=0 mem=0K avg=0.0 table=0K connvals=0K
    ...
```
