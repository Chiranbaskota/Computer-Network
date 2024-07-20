# Wireshark IPv6 Packet Analysis

This repository contains a Wireshark capture file filtered for IPv6 traffic and an analysis of the captured packets.

## Filtering IPv6 Traffic in Wireshark

To filter for IPv6 traffic in Wireshark, use the following display filter:


This filter will display only the packets that use the IPv6 protocol.

## Captured Packets Analysis

### Packet Details

1. **Packet 1**
   - **Source Address**: `2400:1a00:b1e0:6cf1:b03b:54d7:3e7b:240c`
   - **Destination Address**: `2a03:ec00:b95d:bca4:43c4:e9cd:edf4:452a`
   - **Protocol**: BitTorrent
   - **Length**: 142 bytes
   - **Info**: Handshake

2. **Packet 2**
   - **Source Address**: `2400:1a00:b1e0:6cf1:b03b:54d7:3e7b:240c`
   - **Destination Address**: `2a03:ec00:b138:5fa:f8b0:14bd:a972:f5e5`
   - **Protocol**: TCP
   - **Length**: 438 bytes
   - **Info**: 60536 → 59827 [PSH, ACK] Seq=1 Ack=1 Win=64800 Len=364

3. **Packet 3**
   - **Source Address**: `2400:1a00:b1e0:6cf1:b03b:54d7:3e7b:240c`
   - **Destination Address**: `2a03:ec00:b15a:3cc5:b0a8:ab0f:6eb4:aa2e`
   - **Protocol**: BitTorrent
   - **Length**: 142 bytes
   - **Info**: Handshake

4. **Packet 4**
   - **Source Address**: `2400:1a00:b1e0:6cf1:b03b:54d7:3e7b:240c`
   - **Destination Address**: `2a03:ec00:b15a:3cc5:5676:14bd:a972:f5e5`
   - **Protocol**: TCP
   - **Length**: 645 bytes
   - **Info**: 60560 → 59827 [PSH, ACK] Seq=1 Ack=1 Win=64800 Len=571

8. **Packet 8**
   - **Source Address**: `2400:1a00:b1e0:6cf1:b03b:54d7:3e7b:240c`
   - **Destination Address**: `2a03:ec00:b15a:3cc5:b0a8:ab0f:6eb4:aa64`
   - **Protocol**: TCP
   - **Length**: 290 bytes
   - **Info**: 60544 → 59827 [PSH, ACK] Seq=1 Ack=1 Win=64800 Len=216

9. **Packet 9**
   - **Source Address**: `2400:1a00:b1e0:6cf1:b03b:54d7:3e7b:240c`
   - **Destination Address**: `2a03:ec00:b15a:3cc5:b0a8:ab0f:6eb4:aa2e`
   - **Protocol**: TCP
   - **Length**: 142 bytes
   - **Info**: [TCP Retransmission] 60561 → 35251 [PSH, ACK] Seq=1 Ack=1 Win=64800 Len=68

## Field Descriptions

- **Version**: Indicates the IP version, which is 6 for IPv6.
- **Traffic Class**: Used for traffic prioritization.
- **Flow Label**: Used for special handling of packet flows.
- **Payload Length**: Length of the data following the IPv6 header.
- **Next Header**: Indicates the type of the next header (e.g., TCP, UDP).
- **Hop Limit**: Number of hops the packet can take before being discarded.
- **Source Address**: The IPv6 address of the sender.
- **Destination Address**: The IPv6 address of the recipient.

## Usage

1. Open the capture file in Wireshark.
2. Apply the IPv6 filter: `ipv6`
3. Analyze the packets based on the provided details.
