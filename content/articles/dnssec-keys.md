Title: DNSSEC Keys, ZSK vs KSK
Date: 2018-08-26T21:40
Tags: dnssec, dns, comparison
Category: research
The table below summarizes the usage and frequency of use for each of
the keys.:


ZSK vs. KSK Comparison
======================
[jtable]
Key, Usage, Frequency of Use
ZSK, Private, Used by authoritative server to create RRSIG for zone data Used somewhat frequently depending on the zone, whenever authoritative zone data changes or re-signing is needed.
ZSK, Public, Used by recursive server to validate zone data RRset Used very frequently, whenever recursive server validates a response
KSK, Private, Used by authoritative server to create RRSIG for ZSK and KSK Public (DNSKEY) Very infrequently, whenever ZSK's or KSK's change (every year or every five years in our examples)
KSK, Public, Used by recursive server to validate DNSKEY RRset Used very frequently, whenever recursive server validates a DNSKEY RRset
[/jtable]

References
==========

-   <https://ftp.yz.yamagata-u.ac.jp/pub/network/isc/dnssec-guide/html/dnssec-guide.html#troubleshooting-unable-to-load-keys>

