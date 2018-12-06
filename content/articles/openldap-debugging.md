Title: OpenLDAP Debugging Levels
Date: 2018-01-14T19:26
Tags: debugging, openldap
Category: research

olcLogLevel: <level> This directive specifies the level at which
debugging statements and operation statistics should be syslogged
(currently logged to the syslogd(8) LOG\_LOCAL4 facility). You must have
configured OpenLDAP --enable-debug (the default) for this to work
(except for the two statistics levels, which are always enabled). Log
levels may be specified as integers or by keyword. Multiple log levels
may be used and the levels are additive. To display what levels
correspond to what kind of debugging, invoke slapd with -d? or consult
the table below. The possible values for <level> are:

Table 5.1: Debugging Levels
[jtable]
Level, Keyword, Description
-1, any enable all debugging
0, , no,  debugging
1, (0x1 trace),  trace function calls
2, (0x2 packets),    debug packet handling
4, (0x4 args),   heavy trace debugging
8, (0x8 conns),  connection management
16, (0x10 BER),   print out packets sent and received
32, (0x20 filter),    search filter processing
64, (0x40 config),    configuration processing
128, (0x80 ACL),   access control list processing
256, (0x100 stats),    stats log connections/operations/results
512, (0x200 stats2),   stats log entries sent
1024, (0x400 shell),    print communication with shell backends
2048, (0x800 parse),    print entry parsing debugging
16384, (0x4000 sync),    syncrepl consumer processing
32768, (0x8000 none),    only messages that get logged whatever log level is
[/jtable]
