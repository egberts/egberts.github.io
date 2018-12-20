Title: Public Nameservers with DNSSEC support
Date: 2018-11-20 15:11
Tags: DNSSEC, dns
Status: published
Category: HOWTO
Summary: An authoritative list of public name servers supporting DNSSEC.


Here is a list of Open DNS servers that can prove that my highly hardened
personal website is a secured and “un-hackable”.  Basically this test was done
using the “dig” tool with ad notation of whether DNSSEC is supported (and a
small notation if ca is supported too)
The command used is:

```bash
dig +dnssec mywebsiteredacted.net. @<nameserver>
# and 'ad' flag appears as authenticated,
# and note any absense of 'ca' flag
```

The safest DNS nameservers that properly deploy DNSSEC are listed below:
[jtable]
DNSSEC support, IP address,  Name of Nameserver Provider
YES,     185.228.168.9           ,  CleanBrowsing DNS
YES,     185.228.169.9           ,  CleanBrowsing DNS
YES,     156.154.70.1            ,  DNS Advantage
YES,     156.154.71.1            ,  DNS Advantage
YES,     84.200.69.80            ,  DNS Watch
YES,     84.200.70.40            ,  DNS Watch
YES,     216.146.35.35           ,  Dyn
YES,     216.146.36.36           ,  Dyn
YES,     81.218.119.11           ,  GreenTeamDNS
YES,     74.82.42.42             ,  HurricaneElectric
YES,     156.154.70.1            ,  NeuStar
YES,     156.154.71.1            ,  NeuStar
YES,     9.9.9.9                 ,  Quad9
YES,     149.112.112.112         ,  Quad9
[/jtable]
If you are using any of the DNS servers below this line, then when you visit
your banking website, your transaction will not be safe:
[jtable]
DNSSEC support, IP address,  Name of Nameserver Provider
YES,     199.85.126.10           ,  Norton ConnectSafe (discontinued)
YES,     199.85.126.20           ,  Norton ConnectSafe (discontinued)
YES,     199.85.127.10           ,  Norton ConnectSafe (discontinued)
no,       1.0.0.1                ,   Cloudflare
no,       109.69.8.51            ,   puntCAT
no,       1.1.1.1                ,   Cloudflare
no,       176.103.130.130        ,   AdGuard
no,       176.103.130.131        ,   AdGuard
no,       176.103.130.132        ,   AdGuard Family
no,       176.103.130.134        ,   AdGuard Family
no,       195.46.39.39           ,   SafeDNS
no,       195.46.39.40           ,   SafeDNS
no,       198.101.242.72         ,   AlternateDNS
no,       209.244.0.3            ,   Level 3
no,       209.244.0.4            ,   Level 3
no,       23.253.163.53          ,   AlternateDNS
no,       37.235.1.174           ,   FreeDNS
no,       37.235.1.177           ,   FreeDNS
no,       77.88.8.1              ,   YandexDNS
no,       77.88.8.8              ,   YandexDNS
no,       8.8.4.4                ,   Google DNS
no,       8.8.8.8                ,   Google DNS
no,       89.233.43.71           ,   UncensoredDNS
no,       91.239.100.100         ,   UncensoredDNS
no,       bind.odvr.dns-oarc.net ,   DNS OARC
no NOcd,  208.67.220.123         ,   OPENDNS FamilyShield
no NOcd,  208.67.220.220         ,   OPENDNS
no NOcd,  208.67.222.123         ,   OPENDNS FamilyShield
no NOcd,  208.67.222.222         ,   OPENDNS
no NOcd,  8.20.247.20            ,   Comodo
no NOcd,  8.26.56.26             ,   Comodo
[/jtable]
