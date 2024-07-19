**DHCP Process Explained**

This document explains the process of obtaining an IP address from a DHCP server based on captured network packets.



**DHCP Process**

1. DHCP Release (Packet 252)
Timestamp: 39.806776585
Source: 192.168.0.3 (client)
Destination: 192.168.0.1 (DHCP server)
Description:
The client releases its current IP address back to the DHCP server, indicating that it no longer needs the address.

3. DHCP Discover (Packet 277)
Timestamp: 71.059738381
Source: 0.0.0.0 (client)
Destination: 255.255.255.255 (broadcast)
Description:
The client broadcasts a DHCP Discover message to locate available DHCP servers. This is the first step in the process of obtaining a new IP address.

4. DHCP Offer (Packet 278)
Timestamp: 71.072201337
Source: 192.168.0.1 (DHCP server)
Destination: 192.168.0.3 (client)
Description:
The DHCP server responds with a DHCP Offer message, offering an IP address to the client. This message includes details of the offered IP address and other configuration information.
5. DHCP Request (Packet 279)
Timestamp: 71.072638176
Source: 0.0.0.0 (client)
Destination: 255.255.255.255 (broadcast)
Description:
The client responds with a DHCP Request message, indicating its acceptance of the offered IP address. This is a formal request to lease the offered IP address.
6. DHCP ACK (Packet 280)
Timestamp: 71.081892865
Source: 192.168.0.1 (DHCP server)
Destination: 192.168.0.3 (client)
Description:
The DHCP server acknowledges the client's DHCP Request with a DHCP ACK message. This message confirms that the IP address is leased to the client, allowing it to use the IP address.
**Summary**
The DHCP process involves several steps:

Release: The client releases its current IP address.

Discover: The client broadcasts a message to discover available DHCP servers.

Offer: The server responds with an offer of an IP address.

Request: The client requests to lease the offered IP address.

Acknowledge: The server acknowledges and leases the IP address to the client.

This exchange ensures that the client obtains a valid IP address and network configuration from the DHCP server.
