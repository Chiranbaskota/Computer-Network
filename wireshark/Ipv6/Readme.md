# Wireshark IPv6 Multicast Listener Report Analysis

This repository contains examples and explanations on how to capture and analyze ICMPv6 Multicast Listener Report messages using Wireshark.

## Overview

Wireshark is a powerful network protocol analyzer used for network troubleshooting, analysis, and development. This guide focuses on capturing and analyzing ICMPv6 Multicast Listener Report messages, which are part of the Multicast Listener Discovery (MLD) protocol in IPv6.

## ICMPv6 Multicast Listener Report Message

ICMPv6 Multicast Listener Report messages are used by IPv6 routers to discover the presence of multicast listeners on their directly attached links. These messages help in the efficient management of multicast traffic within a network.

## Example Capture

Here is an example of captured ICMPv6 Multicast Listener Report messages filtered in Wireshark:


### Explanation of Fields

- *Frame Number*: The sequential number assigned to the frame in the capture.
- *Time*: The timestamp indicating when the frame was captured.
- *Source*: The IPv6 address of the source sending the packet.
- *Destination*: The multicast IPv6 address to which the packet is sent.
- *Protocol*: The protocol used, which is ICMPv6 in this case.
- *Length*: The length of the frame in bytes.
- *Info*: A brief description of the frame.

## How to Capture ICMPv6 Multicast Listener Report Messages

1. *Open Wireshark*: Launch Wireshark on your computer.
2. *Start Capturing*: Click on the interface you want to capture traffic from and start capturing.
3. *Apply IPv6 Filter*: Use the filter ipv6 to focus on IPv6 traffic.
4. *Identify ICMPv6 Messages*: Look for ICMPv6 packets with the description "Multicast Listener Report Message v2".

