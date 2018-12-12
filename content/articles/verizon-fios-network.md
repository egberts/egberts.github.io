Title: Overview of Verizon FiOS Network
date: 2018-11-10T13:28
modified: 2018-11-13T12:56
tags: verizon, isp
category: research
Overview
========

Components, as listed in network order from your PC to the Internet:

<img src="HFC network.png" title="HFC network.png" alt="HFC network.png" width="800" />

Home Network
============

Your home network can be connected in one of three ways:

* Ethernet by ONT direct Cat-5 (preferred)
* Ethernet via Modem Router MoCA coaxial (common)
* Ethernet via Set-Top Box's MoCA coaxial (rare)

Ethernet via ONT direct Cat-5 (preferred)
-----------------------------------------

<img src="Home network via ONT Ethernet.png" title="Home network via ONT Ethernet.png" alt="Home network via ONT Ethernet.png" width="800" />

* Personal Computer
* Cat-5E cabling for 802.3/1000Base-T
* Your firewall (you do do have a firewall?)
* Cat-5E cabling for 802.3/1000Base-T
* ActionTec MI424WR, 4-port wireless broadband modem router, 2-channel MoCA,.
* Cat-5E cabling for 802.3/1000Base-T; no PPP, no PPPoE, no PPTP.  Straight TCP/IP.
* ONT, Motorola 1400, via Ethernet RJ-45 connector

Note: Call FiOS support at 1-888-553-1555. Remember what your mother
taught you: use your manners! The Verizon technician doesn’t have to do
this for you and will be doing you a favor. Ask customer support to
switch the ONT from coaxial output to ethernet output. If they give you
a hard time about doing it remotely, tell them that you want to use your
own router, an ethernet cable is already run, and you don’t need a
technician to come out. You may even need to ask for a supervisor or
level-two support technician. Expect to spend about 30-45 minutes on the
phone.

Ethernet via Modem Router MoCA coaxial (common)
-----------------------------------------------

Most commonly used method by Verizon installer is:

![](Home network via Modem Router MoCA coaxial.png "Home network via Modem Router MoCA coaxial.png")

* Personal Computer
* Cat-5E cabling for 802.3/1000Base-T
* Your firewall
* Cat-5E cabling for 802.3/1000Base-T
* ActionTec MI424WR, 4-port wireless broadband router, 2-channel MoCA
* RG-6 cabling, with F-connectors, MoCA protocol
* ONT, Motorola 1400, coaxial, via F-connector

Ethernet via Set-Top Box's MoCA coaxial (rare)
----------------------------------------------

or that rarely used Ethernet port behind the Set-Top Box

* Personal Computer
* Cat-5E cabling for 802.3/1000Base-T
* Your firewall
* Cat-5E cabling for 802.3/1000Base-T
* Cable Set-Top Box (STB), IP-STB1 cable media gateway (MAC Arris/ResiNet, aka
* DOCSIS Gateway w/ MoCA, aka Digital STB)
* RG-6 cabling, with F-connectors, MoCA protocol
* ONT, Motorola 1400, coaxial, via F-connector
* ISP Network

Then to the ISP Network
-----------------------

then

<img src="Verizon ISP network.png" title="Verizon ISP network.png" alt="Verizon ISP network.png" width="800" />

* Motorola ONT 1400 Single Family Unit (SFU) is an ITU G.984-compliant GPON intelligent optical network terminal (ONT)
* Fiber cable, Single-Mode (SM), SC connector
* MTP/MTO optical splitter, 4:1, on telephone poles
* Optical Nodes
* Trunk Fiber cable, Single-Mode (SM)
* Head-End

Head-End
--------

Head-End comprises of the following:

* Trunk Fiber cable, Single-Mode (SM)
* EQAM (mixes cable and data)
* Switch, Juniper EX3300, 24-Port PoE+ GE/4-Port SFP+ AC
* Hybrid Fiber Coaxial (HFC) network
* CMTS
* CATV

Technical Evolution
===================

<table>
<thead>
<tr class="header">
<th><p>DOCSIS RELEASE</p></th>
<th><p>MAX DOWNLOAD</p></th>
<th><p>MAX UPLOAD</p></th>
<th><p>DATE RELEASED</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>DOCSIS 1</p></td>
<td><p>40 Mbps</p></td>
<td><p>10 Mbps</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>DOCSIS 1.1</p></td>
<td><p>40 Mbps</p></td>
<td><p>10 Mbps</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>DOCSIS 2</p></td>
<td><p>40 Mbps</p></td>
<td><p>30 Mbps</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>DOCSIS 2.5</p></td>
<td><p>-</p></td>
<td><p>--</p></td>
<td><p>Discontinued use of RG-59 cable</p></td>
</tr>
<tr class="odd">
<td><p>DOCSIS 3</p></td>
<td><p>1.2 Gbps</p></td>
<td><p>200 Mbps</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>DOCSIS 3.1</p></td>
<td><p>10 Gbps</p></td>
<td><p>1 Gbps</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>DOCSIS 3.1 Full Duplex</p></td>
<td><p>10 Gbps</p></td>
<td><p>10 Gbps</p></td>
<td><p>2015</p></td>
</tr>
</tbody>
</table>

Equipments
==========

GPON ONT
--------

* SFH ONT 612AZ
* \[<https://www.actiontec.com/products/wifi-routers-gateways/fiber/bhr-rev-i/>
* Motorola ONT 1400\]

<table>
<thead>
<tr class="header">
<th><p>Manufacturer</p></th>
<th><p>Model</p></th>
<th><p>Type</p></th>
<th><p>Style</p></th>
<th><p>MoCA/Coax</p></th>
<th><p>Ethernet/VDSL2</p></th>
<th><p>POTS</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Alcatel</p></td>
<td><p>I-211M-L</p></td>
<td><p>SFU</p></td>
<td><p>Interior Desktop</p>
<p>Exterior</p></td>
<td><p>1: MoCA</p></td>
<td><p>1: 10/100/1G Ethernet</p></td>
<td><p>2</p></td>
</tr>
<tr class="even">
<td><p>Alcatel</p></td>
<td><p>O-24121G-A</p></td>
<td><p>MDU</p></td>
<td><p>Shared</p></td>
<td><p>12</p></td>
<td><p>12: 10/100/1G Ethernet</p></td>
<td><p>24</p></td>
</tr>
<tr class="odd">
<td><p>Alcatel</p></td>
<td><p>O-24121V-A</p></td>
<td><p>MDU</p></td>
<td><p>Shared</p></td>
<td><p>12</p></td>
<td><p>12: VDSL2</p></td>
<td><p>24</p></td>
</tr>
<tr class="even">
<td><p>Alcatel</p></td>
<td><p>O-821M-A</p></td>
<td><p>SOHO</p></td>
<td><p>Exterior</p></td>
<td><p>1: MoCA</p></td>
<td><p>2: 10/100/1G Ethernet</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>Motorola</p></td>
<td><p>1000-GI4</p></td>
<td><p>SFU</p></td>
<td><p>Interior</p></td>
<td><p>1: MoCA</p></td>
<td><p>1: 10/100/1G Ethernet</p></td>
<td><p>2</p></td>
</tr>
<tr class="even">
<td><p>Motorola</p></td>
<td><p>1000-GJ4</p></td>
<td><p>SFU</p></td>
<td><p>Interior</p></td>
<td><p>1: MoCA</p></td>
<td><p>1: 10/100/1G Ethernet</p></td>
<td><p>2</p></td>
</tr>
<tr class="odd">
<td><p>Motorola</p></td>
<td><p>1000-GT4</p></td>
<td><p>SFU</p></td>
<td><p>Exterior</p></td>
<td><p>1: MoCA</p></td>
<td><p>1: 10/100/1G Ethernet</p></td>
<td><p>2</p></td>
</tr>
<tr class="even">
<td><p>Motorola</p></td>
<td><p>14842</p></td>
<td><p>SOHO</p></td>
<td><p>Exterior</p></td>
<td><p>1: MoCA</p></td>
<td><p>5: 10/100/1G Ethernet</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>Motorola</p></td>
<td><p>6000-GET</p></td>
<td><p>MDU</p></td>
<td><p>Shared</p></td>
<td><p>1: MoCA</p></td>
<td><p>12: 10/100/1G Ethernet</p></td>
<td><p>24</p></td>
</tr>
<tr class="even">
<td><p>Motorola</p></td>
<td><p>6000-GVT</p></td>
<td><p>MDU</p></td>
<td><p>Shared</p></td>
<td><p>1: MoCA</p></td>
<td><p>12: VDSL2</p></td>
<td><p>24</p></td>
</tr>
</tbody>
</table>

Legend:

* SFU Exterior (ONT Outside of Home): An ONT is installed outside. The
    battery
* backup unit (BBU) and power supply (PS) are installed inside. The PS
    must be
* within 6 feet of a grounded outlet. The PS can be up to 50 feet from
    the BBU.
* SFU Exterior installs are now only done if an SFU Interior is
    not feasible.
* SFU Interior (ONT Wall-Mounted Inside of Home): An All-In-One ONT is
    usually
* used on house interior installs. The ONT, BBU (if applicable) and PS
    are in a
* single enclosure. SFU Interior is the most common type of install.
* SFU Desktop (ONT Self-Standing Inside of Home): A small ONT is
    placed inside
* the house, not wall mounted. This setup is used if wall space
    is limited.
* Desktop ONTs can also be wall mounted inside or outside, in
    an enclosure. This
* makes them the most versatile, and therefore most common type of
    ONT used.
* SOHO Exterior (ONT Outside of Office): Same as SFU Exterior, except
    the ONT
* has extra Ethernet and Telephone ports for the
    Office/Small Business.

Phased out:

* MDU Shared (ONT in Shared Location for Apartments and Condos): A
    shared ONT
* is placed in the apartment or condo building. Speeds are limited to
    anywhere
* from 15/5 to 75/75, depending on the ONT, and FiOS Digital Voice is
    not
* available. There is, however, FiOS Freedom Essentials, which
    isn't VoIP.

Modem Router
------------

DOCSIS 3.0 MoCA Modem Routers:

* \[<https://www.actiontec.com/products/wifi-routers-gateways/fiber/bhr-rev-i/>
* ActionTec MI424WR\]
* Fios Quantum Gateway

Set-Top Box
-----------

* Motorola QIP2500 (S-video, composite \[RCA\], Coax)
* Motorola 7232-P2, Multi-Room DVR
* Motorola 7216, HD DVR
* Motorola 7100-P2 HD Set-top Box
* Motorola 7100-P1 HD Set-top Box
* Cisco CHS 435 HD DVR
* Cisco CHS 335 HD Set-top Box

Terminologies
=============

* CMTS - Cable Modem Termination System
* Directional Coupler - Similar to a splitter but with a different attenuation between output ports. Generally there is one main output that has little attenuation and a second output that has more attenuation.
* DOCSIS - Data Over Cable System Interface Specification, Cable TV's data protocol
* Node - any device that connects to the MoCA network
* ONT - Optical Network Termination
* STB - Set-Top Box - Any device that feeds audio and video signals to a television. These are generally cable, satellite, or IP inputs.
* Telco - Telephone Company Service Provider
* WECB - Wi-Fi Ethernet Coax Bridge - a bridge which converts between Wi-Fi,
* Ethernet, and/or MoCA in any combination.

References
==========

* <https://www.cablelabs.com/specs/>
* <https://www3.nd.edu/~cpoellab/teaching/cse40815/Chapter6.pdf>
* <http://www.lightreading.com/cable-video/docsis/docsis-31-targets-10-gig-downstream/d/d-id/699136>
* <https://apps.fcc.gov/edocs_public/attachmatch/FCC-16-6A1.pdf>
* <http://www.klonex.com.pl/media/produkty/pdf/motorola-ont1400gt.pdf>
* <https://forums.verizon.com/t5/Fios-Internet/Using-your-own-router-with-Verizon-FiOS/td-p/851632>

