Title: Bind9 Directories
Date: 2018-10-18 18:56
slug: bind9-directories
tags: bind9
category: research
summary: Directories used by ISC Bind9

Bind9 directories
=================
[jtable]
directory name, named.conf keyword, description
/etc/bind, directory, directory is a quoted string defining the absolute path for the server e.g. &quot;/var/named&quot;. All subsequent relative paths use this base directory. If no directory options is specified the directory from which BIND was loaded is used. This option may only be specified in a 'global' options statement.
<code>/etc/bind</code>, <code>file</code>, zone files
<code>/etc/bind/keys</code>, <code>key-directory</code>, "key-directory is a quoted string defining the absolute path, for example, &quot;/var/lib/bind/dynamic&quot; where the keys used in the dynamic update of secure zones may be found. Only required if this directory is different from that defined by a directory option. This statement may only be used in a global options clause. <code>rndc</code> <code>loadkeys</code> and <code>rndc</code> <code>sign</code> reads from this directory. "
<code>/var/lib/bind</code>, ,
<code>/var/lib/bind/dynamic</code>, <code>managed-keys-directory</code>, Zone files
<code>/etc/default/bind</code>, , Default systemd settings for <code>named</code> daemon startup (<a href="bind9.service" class="uri" title="wikilink">bind9.service</a>)
<code>/var/cache/bind</code>, <code>key-directory</code>, Dynamically created keyfiles
<code>/var/log/bind</code>, , logging for DNS <code>named</code> daemon
[/jtable]


Bind9 files
===========
[jtable]
file name, named.conf keyword, description
<code>/var/run/named/named.pid</code>, <code>pid-file</code>, "PID number of the master named process, in text-format. pid-file is a quoted string and allows you to define where the pid (Process Identifier) used by BIND is written. If not present it is distribution or OS specific typically /var/run/named.pid or /etc/named.pid. It may be defined using an absolute path or relative to the directory parameter. This statement may only be used in a global options clause. "
<code>/etc/bind/rndc.conf</code>, , "Used by <code>rndc</code> utility. Manually created and often formatted like:</p>, <code>   # Start of rndc.conf</code><br /> <code>   include &quot;/etc/bind/rndc.key&quot;;</code><br /> <code>   options {</code><br /> <code>       default-key &quot;rndc-key&quot;;</code><br /> <code>       default-server 127.0.0.1;</code><br /> <code>       default-port 953;</code><br /> <code>   };</code><br /> <code>   # End of rndc.conf</code>"
<code>/etc/bind/rndc.key</code>, , its key is created using <code>rndc-confgen</code> <code>-a</code> looking like this:</p> <p><code>   key &quot;rndc-key&quot; {</code><br /> <code>       algorithm hmac-md5;</code><br /> <code>       secret &quot;XbAxWyZPL74rN1Ti3dTV9a==&quot;;</code><br /> <code>   };</code>
<code>/var/cache/bind/&#42.jnl</code>, <code>journal</code>, Keeps track of changes being made to the zone databases
<code>/var/cache/bind/cache_dump.db</code>, <code>dump-file</code>, "Dumps the DNS cache database into a text file. dump-file is a quoted string defining the absolute path where BIND dumps the database (cache) in response to a rndc dumpdb. If not specified, the default is named_dump.db in the location specified by a directory option. This option may only be specified in a 'global' options statement. "
<code>/var/log/bind/named_stats.txt</code>, <code>statistics-file</code>, Dumps the statistics into a file. This statement defines the file-name to which data will be written when the command rndc stats is issued. May be an absolute or relative (to directory) path. If the parameter is not present the information is written to named.stats in the path defined by directory or its default. This statement may only be used in a global options clause.
<code>/var/log/mem-statistics.log</code> , <code>memstatistics-file</code> , This statement defines the file-name to which BIND memory usage statistics will be written when it exits. May be an absolute or relative (to directory) path. If the parameter is not present the stats are written to <code>named.memstats</code> in the path defined by directory or its default. This statement may only be used in a global options clause.
<code>/etc/bind/named.iscdlv.key</code> , <code>bindkeys-file</code> , OBSOLETED. Holds the DLV (now discontinued as of Feb 2017). Used to be <code>/etc/bind.keys</code>
[/jtable]

Bind9 logging channels
======================
[jtable]
directory name, channel name , description
<code>/var/log/bind/default.log</code> , <code>default_file</code> , Default events get logged into this file
<code>/var/log/bind/general.log</code> , <code>general_file</code> , General events get logged into this file.
<code>/var/log/bind/database.log</code> , <code>database_file</code> , Database events get logged into this file.
<code>/var/log/bind/security.log</code> , <code>security_file</code> , Security events get logged into this file.
<code>/var/log/bind/config.log</code> , <code>config_file</code> , Configuration and any misconfiguration events get logged into this file.
<code>/var/log/bind/resolver.log</code> , <code>resolver_file</code> , Resolver events get logged into this file.
<code>/var/log/bind/xfer-in.log</code> , <code>xfer-in_file</code> , Transfer DNS records inbound events get logged into this file.
<code>/var/log/bind/xfer-out.log</code> , <code>xfer-out_file</code> , Transfer DNS records outbound events get logged into this file.
<code>/var/log/bind/notify.log</code> , <code>notify_file</code> , Notify events get logged into this file.
<code>/var/log/bind/unmatched.log</code> , <code>client_file</code> , Client events get logged into this file.
<code>/var/log/bind/client.log</code> , <code>unmatched_file</code> , Unmatched events get logged into this file.
<code>/var/log/bind/unmatched.log</code> , <code>unmatched_file</code> , Unmatched events get logged into this file.
<code>/var/log/bind/queries.log</code> , <code>queries_file</code> , Query events get logged into this file.
<code>/var/log/bind/query-errors.log</code>
, <code>query-errors_file</code>
, Query ERROR events get logged into this file.
<code>/var/log/bind/network.log</code>
, <code>network_file</code>
, "Network events get logged into this file. open(), close(), dropped or downed network interface."
<code>/var/log/bind/update.log</code> , <code>update_file</code> , Update events get logged into this file.
<code>/var/log/bind/update-security.log</code> , <code>update-security_file</code> , Security update events get logged into this file.
<code>/var/log/bind/dispatch.log</code> , <code>dispatch_file</code> , Dispatch events get logged into this file.
<code>/var/log/bind/dnssec.log</code> , <code>dnssec_file</code> , DNSSEC events get logged into this file.
<code>/var/log/bind/lame-servers.log</code> , <code>lame-servers_file</code> , Lame server events get logged into this file.
<code>/var/log/bind/delegation-only.log</code> , <code>delegation-only_file</code> , Delegation events get logged into this file.
<code>/var/log/bind/rate-limit.log</code> , <code>rate-limit_file</code> , Rate limiting events get logged into this file.

[/jtable]
