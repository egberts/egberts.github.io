title: Comparison of VPN specification
date: 2018-07-17 13:01
tags: comparison, vpn
status: published
category: research
summary: A comparison of VPN and its specification.

[jtable]
Comparison, PPTP, L2TP, <a href="OpenVPN" class="uri" title="wikilink">OpenVPN</a>, IPSec
VPN Encryption , 128-bit , 256-bit , 160-bit <br> 256-bit , 256-bit |-<br>
Manual Setup Supported , Windows <br> Mac OS X <br> Linux <br> iOS <br> Android <br> DD-WRT , Windows <br> Mac OS X <br> Linux <br> iOS <br> Android , Windows <br> Mac OS X <br> Linux <br> iOS <br> Android , Windows <br> Mac OS X <br> Android
VPN Security , Basic encryption , Highest encryption. Checks data integrity and encapsulates the data twice.  , Highest encryption. Authenticates data with digital certificates.  , Highest encryption. Authenticates data with digital certificates.
VPN Speed , Fast due to lower encryption. , Requires more CPU processing to encapsulate data twice. , "Best performing protocol. Fast speeds even on connections with high latency and across great distances." , Best performing protocol. Defeats deep packet inspection. Fast speeds; even on connections with high latency and across great distances.
Stability , Works well on most Wi-Fi hotspots very stable. , Stable on NAT-supported devices., Most reliable and stable; even behind wireless routers; on non-reliable networks; and on Wi-Fi hotspots., Masks VPN traffic so it cannot be identified as a VPN connection (via deep packet inspection) and blocked.
Compatibility , Native in most desktop; mobile device and tablet operating systems., Native in most desktop; mobile device and tablet operating systems., Supported by most desktop computer operating systems and Android mobile and tablet devices., Supported by most desktop computer operating systems and Android mobile and tablet devices.
Conclusion , PPTP is a fast; easy-to-use protocol. It is a good choice if OpenVPN isn't supported by your device., L2TP/IPsec is a good choice if OpenVPN isn't supported by your device and security is top priority., OpenVPN is the recommended protocol for desktops including Windows/Mac OS X/Linux. Highest performance - fast, secure and reliable.", "Chameleon is great for VPN users being blocked in countries such as China, or if you are experiencing speed issues due to bandwidth throttling."
[/jtable]

Technical features
------------------


<td>
<p><ref name="acevpn-openvpn">{{cite web |url=<a href="https://www.acevpn.com" class="uri">https://www.acevpn.com</a>
<td><p>"title=Fast, Secure, Anonymous VPN and Smart DNS Service. Free Installation"
<td><p>work=Multiple Devices and Protocols |deadurl=no
<td><p>archiveurl=<a href="https://web.archive.org/web/20180103183838/https://www.acevpn.com/" class="uri">https://web.archive.org/web/20180103183838/https://www.acevpn.com/</a>
<td><p>archivedate=2018-01-03 }}</ref>
<td></td>
</tr>
</tbody>
</table>

Website
-------

![](Antipat4.svg "fig:Antipat4.svg")|Library [warrant
canary](warrant_canary "wikilink") relying on active removal designed by
[Jessamyn West](Jessamyn_West_(librarian) "wikilink").\]\] The rating of
the services' websites according to SSL server certificate and HTTP
cookie test tools. Also listed is whether the websites maintain a
[warrant canary](warrant_canary "wikilink").

<table>
<thead>
<tr class="header">
<th><p>Service</p></th>
<th><p><a href="Public_key_certificate#TLS/SSL_server_certificate" title="wikilink">SSL certificate</a></p></th>
<th><p><a href="#Privacy_Impact_Score" title="wikilink">Privacy Impact Score</a></p></th>
<th><p><a href="#Warrant_canary" title="wikilink">Warrant canary</a></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="#Holder" title="wikilink">Holder</a>
<td><p><a href="#Issued_to" title="wikilink">Issued to</a>
<td><p>data-sort-type=&quot;number&quot; | <a href="#SSL_Rating" title="wikilink">SSL rating</a>
</tr>
<tr class="even">
<td><p><a href="AceVPN" class="uri" title="wikilink">AceVPN</a>
<td>
<p><ref name="ssltest-acevpn">{{cite web
<td><p>url=<a href="https://www.ssllabs.com/ssltest/analyze.html?d=acevpn.com&amp;s=104.28.23.38" class="uri">https://www.ssllabs.com/ssltest/analyze.html?d=acevpn.com&amp;s=104.28.23.38</a>
<td><p>title=SSL Server Test: acevpn.com (Powered by Qualys SSL Labs) |deadurl=no
</tr>
</tbody>
</table>
