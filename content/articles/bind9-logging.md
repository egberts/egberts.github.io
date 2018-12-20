Title: ISC Bind9 Logging
Date: 2018-10-17 10:41
Tags: logging, bind9
Category: research
summary: Logging Files Used By ISC Bind9
Editing Bind9 logging Bind9 logging is controlled and ferrated into
several channels.

Functional Log
--------------
Bind9 log channel categories.
[jtable]
category name, source files
NS_LOGCATEGORY_CLIENT, client.c
DNS_LOGCATEGORY_DATABASE, lwdclient.c
NS_LOGCATEGORY_GENERAL, "lwdclient.c, lwresd.c, main.c, server.c, statschannel.c, tkeyconf.c"
NS_LOGCATEGORY_NETWORK, interfacemgr.c
NS_LOGCATEGORY_NOTIFY, notify.c
DNS_LOGCATEGORY_DNSSEC, query.c
NS_LOGCATEGORY_QUERIES, query.c
NS_LOGCATEGORY_QUERY_EERRORS, "client.c, query.c"
NS_LOGCATEGORY_RPZ, query.c
DNS_LOGCATEGORY_RRL, query.c
DNS_LOGCATEGORY_SECURITY, query.c
NS_LOGCATEGORY_UNMATCHED, client.c
NS_LOGCATEGORY_UPDATE, update.c
NS_LOGCATEGORY_UPDATESECURITY, update.c
DNS_LOGCATEGORY_XFER_OUT, xferout.c
[/jtable]


Log modules
-----------
Bind9 log channel modules

[jtable]
module name, source files
NS_LOGMODULE_ADB, lwdclient.c
NS_LOGMODULE_CLIENT, client.c
NS_LOGMODULE_INTERFACEMGR, interfacemgr.c
NS_LOGMODULE_MAIN, main.c
NS_LOGMODULE_NOTIFY, notify.c
NS_LOGMODULE_QUERY, query.c
NS_LOGMODULE_SERVER, main.c
NS_LOGMODULE_UPDATE, update.c
NS_LOGMODULE_XFER_OUT, xferout.c
[/jtable]

