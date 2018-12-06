Title: Bro-IDS HOWTO
Date: 2017-11-01 05:11
Category: HOWTO
Tags: Bro
summary: How to use Bro IDS.

How to use Bro

Repository
==========

To obtain Bro:

```bash
git clone https://github.com/bro-ids/bro
```

And their dependent packages

```bash
sudo yum install mongodb-devel
sudo service bro start
sudo yum install cmake28
sudo alternatives --install /usr/bin/cmake cmake /usr/bin/cmake28 90
sudo yum install python-devel
```

Installation
============

Configure installation using default settings:

```bash
./configure --enable-debug \
   --disable-broccoli --prefix=/usr --conf-files-dir=/etc/bro
make
sudo make install  # goes into /usr/local
```

Bro executable
==============

Command line options General usage:

```bash
bro [option] <bro-policy-script-file>
```

[jtable]
option, long option, description
`-a`, `--parse-only`, "Syntax check the policy script files. bro returns 0 if OK, 1 if syntax is invalid (new in Bro 2.3.1)
`-b`, `--bare-mode`, Don't load scripts from the base/ directory. Useful in testing
`-d`, `--debug-policy`, Activate policy file debugger
`-e`, `--exec`, augment loaded policies by given script code
`-f`, `--filter`, tcpdump BPF filter (ie. `port 22 or udp and icmp`) (see BFP syntax (external site)
`-g`, `--dump-config`, Dumps current configuration into the ./.state subdirectory
`-i`, `--iface`, Read from given network interface
`-p`, `--prefix`, Add given prefix to policy filepath resolution. This is also BRO_PREFIXES environment variable. Contains a list of subdirectories separated by a semicolon in which to search a policy file for. A @load .bro statement in the script would result in searching each BRO_PREFIXES subdirectories in the order given in which to load .bro script file from.
`-r`, `--readfile`, PCAP file in which to read from (instead of from a network interface.)
`-s`, `--rulefile`, Read rules from a given file. Useful for Signature RULE testing.
`-t`, `--tracefile`, Outputs a trace execution of each line of each script file loaded
`-N`, `--print-plugins`, Print available plugins and exit
`-N`, `--print-plugins`, -print-plugins Print event and function available in each plugins (verbose)
`-S`, `--debug-rules`, Enable rule debugging. More about setting up the rule tables and less about rule matching.
[/jtable]

Bro Environment Variables
-------------------------

[jtable]
environment name , program , environment description
`BROPATH` , bro , "file search path for Bro policy script; A list of directory, each separated by semicolon, in which profile script files can be searched for."
`BRO_DNS_FAKE` , bro , disable DNS lookups; Determine whether actual DNS lookup occurs or fake DNS data is returned; Valid value: '0' or '1'.
`BRO_SEED_FILE` , bro , A filespec to a file containing seed number for the Bro's init_random_seed(); useful for ensuring repeatable test runs.
`BRO_PREFIXES` , bro , add given prefix to policy file resolution; this adds a full or relative directory path to try for each script file given
`BRO_LOG_SUFFIX` , bro , ASCII log file extension (currently set to .log)
`BRO_PROFILER_FILE` , bro , Full or relative filespec where to put the Bro profiler data in. A presense of this environment variable is the only way to turn this Bro profiler on.
`BRO_DISABLE_BROXYGEN` , bro , Disable the Broxygen documentation
`CLUSTER_NODE` , bro , broctl
`BROCTL_INSTALL_PREFIX` , broctl , Where did broctl get installed to? (occurrs during bro install time)
`BRO_ARG_TESTBRO` , btest ,
`NOTDEFINED` , btest ,
`TESTBRO` , btest ,
`BROCCOLI_CONFIG_FILE` , broccoli , Broccoli configuration filespec
[/jtable]


UNIX Signal supported
=====================
[jtable]
Signal name , Signal description
`SIGINT` , "From main process, calls bro_done() events. From main process, kills all threads if SIGINT received the 2nd time. Not used in threads. With -d mode, it caused Bro policy script debugger prompt to appear (requires an active STDIN/STDOUT terminal.)"
`SIGTERM` , "From main process, calls bro_done() events. From main process, kills all threads if SIGTERM received the 2nd time. Main process may send to child thread for terminating RAW input reader(s). With -dmode, it caused Bro policy script debugger prompt to appear (requires an active STDIN/STDOUT terminal.)"
`SIGSTOP` , "broctl sends STOP signal firstly to all Bro manager, proxy(s), and workers first time around, then KILL on 2nd try."
`SIGPIPE` , "With -d mode, this signal gets ignored. RAW input reader(s) inherits main process SIGPIPE in Raw::Execute()."
`SIGHUP` , "During bro.init(), checkpoints persistent state."
`SIGALRM` , Main process uses it monitor for jammed or idle network interface(s). Thread uses to request stats to be sent. sig_handler_log()
`SIGPROF` , "Thread uses it to request CPU usage statistics to be sent to SocketComm::Log (remote.log) via sig_handler_prof(). If compiled with DEBUG_COMMUNICATION (src/ChunkedIO.h), main process uses it to dump debug data of RemoteSerializer then terminate."
`SIGKILL` , Propagates from thread/child to main process.
`SIGUSR1` , Used to be used for MPatrol debugging hooks. Not used in threads.
`SIGUSR2` , Used to be used for MPatrol debugging hooks. Not used in threads.
`SIGCONT` , Not used in threads.
`SIGQUIT` , QUIT is sent in event of RemoteSerializer::FatalError() toward child process(es).
`SIGCHLD` , Not used in threads.
`SIGSEGV` , Propagates from thread/child to main process.
`SIGBUS` , Propagates from thread/child to main process.
`SIGFPE` , Propagates from thread/child to main process.
[/jtable]

External References
===================

1.  Bro Documentation - <http://mailman.icsi.berkeley.edu/mailman/listinfo/bro-announce>
2.  Bro Support - <https://www.bro.org/support/>
3.  Bro Contacts - <https://www.bro.org/contact/>

Mailing List
============

1.  General - <http://mailman.icsi.berkeley.edu/mailman/listinfo/bro>
2.  Announcement - <http://mailman.icsi.berkeley.edu/mailman/listinfo/bro>
2.  Twitter - @Bro_IDS
3.  IRC - Freenode's \#bro channel
4.  Bro Community - <https://www.bro.org/community/>
5.  Index to all of Bro website - <https://www.bro.org/sphinx/genindex.html>

