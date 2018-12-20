DHCP Lease Renewal and Rebinding Processes
##########################################

:Tags: dhcp
:Date: 2018-10-14 16:31
:Category: research

DHCP Lease Renewal and Rebinding Processes
==========================================

Lease Renewal/Rebinding Process Steps
-------------------------------------

The following steps summarize the renewal/rebinding process. Obviously,
the exact sequence of operations taken by a client depends on what
happens in its attempts to contact a server; for example, if it is
successful with renewal, it will never need to attempt rebinding. An
example renewal and rebinding is illustrated in Figure 265. Note also
that the same notes about addressing fields, relay agents and such that
I mentioned in the allocation process topic apply here as well.

.. figure:: /images/Dhcprere.png
   :width: 440px
   :align: center
   :height: 400px
   :alt: DHCP Lease Renewal and Rebinding Process
   :figclass: align-center

   DHCP Lease Renewal and Rebinding Process.


This diagram shows the example of a client that presently holding a
lease with Server \#2 attempting to contact it to renew the lease.
However, in this case, Server \#2 is down for maintenance. The server is
unable to respond and the client remains stuck at Step \#2 in the
renewal/rebinding process. It keeps sending DHCPREQUEST messages to
Server \#2 until its T2 timer expires. It then enters the rebinding
state and broadcasts a DHCPREQUEST message, which is heard by Server
\#1, which in this case agrees to extend its current lease.

Renewal Timer (T1) Expires
==========================

The renewal timer, T1, is set by default to 50% of the length of the
lease. When the timer goes off, the client transitions from the BOUND
tate to the RENEWING state.

Note that a client may initiate lease renewal prior to T1 timer
expiration if it desires.

1. Client Sends DHCPREQUEST Renewal Message
===========================================

The client creates a DHCPREQUEST message that identifies itself and its
lease. It then transmits the message directly to the server that
initially granted the lease, unicast. Note that this is different from
the DHCPREQUEST messages used in the allocation/reallocation processes,
where the DHCPREQUEST is broadcast. The client may request a particular
new lease length, just as it may request a lease length in its requests
during allocation, but as always, the server makes the final call on
lease length.


2. Server Receives and Processes DHCPREQUEST Message and Creates Reply
======================================================================

Assuming the server is reachable, it will receive and process the
client's renewal request. There are two possible responses:

* Server Agrees To Renew Client Lease: The server decides that the client's lease can be renewed. It prepares to send to the client a DHCPACK message to confirm the lease's renewal, indicating the new lease length and any parameters that may have changed since the lease was created or last renewed.
* Server Refuses To Renew Client Lease: The server decides for whatever reason not to renew the client's lease. It will create a DHCPNAK message.

4. Server Sends Reply
=====================


The server sends the DHCPACK or DHCPNAK message back to the client.

5. Client Receives and Processes Server Reply
=============================================

The client takes the appropriate action in response to the server's
reply:

* Positive Acknowledgment: The client receives a DHCPACK message, renewing the lease. The client makes note of the new lease expiration time and any changed parameters sent by the server, resets the T1 and T2 timers, and transitions back to the BOUND state. Note that the client does not need to do an ARP IP address check when it is renewing.
* Negative Acknowledgment: The message is a DHCPNAK, which tells the client that its lease renewal request has been denied. The client will immediately transition to the INIT state to get a new lease—step \#1 in the allocation process.

6. Rebinding Timer (T2) Expires
===============================

If the client receives no reply from the server, it will remain in the
RENEWING state, and will regularly retransmit the unicast DHCPREQUEST to
the server. During this period of time, the client is still operating
normally, from the perspective of its user. If no response from the
server is received, eventually the rebinding timer (T2) expires. This
will cause the client to transition to the REBINDING state. Recall that
by default, the T2 timer is set to 87.5% (7/8ths) of the length of the
lease.

7. Client Sends DHCPREQUEST Rebinding Message
=============================================

Having received no response from the server that initially granted the
lease, the client “gives up” on that server and tries to contact any
server that may be able to extend its existing lease. It creates a
DHCPREQUEST message and puts its IP address in the CIAddr field,
indicating clearly that it presently owns that address. It then
broadcasts the request on the local network.

8. Servers Receives and Processes DHCPREQUEST Message and Send Reply
====================================================================

Each server receives the request, and responds according to the
information it has for the client (a server that has no information
about the lease or may have outdated information does not respond):

* Server Agrees To Rebind Client Lease: A server has information about the client's lease and agrees to extend it. It prepares for the client a DHCPACK message to confirm the lease's renewal, indicating any parameters that may have changed since the lease was created or last renewed.
* Server Decides Client Cannot Extend Its Current Lease: A server determines that for whatever reason, this client's lease should not be extended. It gets ready to send back to the client a DHCPNAK message.

9. Server Sends Reply
=====================

Each server that is responding to the client sends its DHCPACK or
DHCPNAK message.

10. Client Receives Server Reply
================================

The client takes the appropriate action in response to the two
possibilities in the preceding step:

* Positive Acknowledgment: The client receives a DHCPACK message, rebinding the lease. The client makes note of the server that is now in charge of this lease, the new lease expiration time, and any changed parameters sent by the server. It resets the T1 and T2 timers, and transitions back to the BOUND state. (It may also probe the new address as it does during regular lease allocation.)
* Negative Acknowledgment: The message is a DHCPNAK, which tells the client that some server has determined that the lease should not be extended.  The client immediately transitions to the INIT state to get a new lease—step \#1 in the allocation process.

11. Lease Expires
=================

If the client receives no response to its broadcast rebinding request,
it will, as in the RENEWING state, retransmit the request regularly. If
no response is received by the time the lease expires, it transitions to
the INIT state to get a new lease.
