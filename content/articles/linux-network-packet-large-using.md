Title: Using Large Network Packet
Date: 2018-09-24T09:38
category: research
tags: ethernet, packet
Your customer is using large network packets. And by large packets, this
means packet size greater than 1514 bytes.

In computer networking, the maximum transmission unit (MTU) of a
communications protocol of a layer is the size (in bytes) of the largest
protocol data unit that the layer can pass onwards. MTU parameters
usually appear in association with a communications interface (NIC,
serial port, etc.). Standards (Ethernet, for example) can fix the size
of an MTU; or systems (such as point-to-point serial links) may decide
MTU at connect time.

Step-by-step guide
==================

Enter root shell

Add MTU to the motherboard NIC (eth0)

```bash
echo "MTU=65535" >> /etc/sysconfig/network-scripts/ifcfg-eth0
```

Turn off hardware-assist offloading on the Ethernet interface.

```bash
# set the MSS
ifconfig eth0 mtu 65535
# turn off TCP offload
ethtool -K eth0 tso off
# turn off GRE offload
ethtool -K eth0 gso off
```

To make it permanent, edit and insert the above code into
\`\`\`/etc/rc.local\`\`\` and reboot.
