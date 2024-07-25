# Network Ping Simulation in Cisco Packet Tracer

This repository provides a detailed explanation of how DHCP works and ICMP packets traverse different networks using Cisco Packet Tracer.

## Network Setup

The network consists of two subnets connected via a router:

- **Network 1**: `10.1.1.0/24`
  - `PC0`: `10.1.1.1`
  - `Laptop0`: `10.1.1.2`
- **Network 2**: `192.168.1.0/24`
  - `PC1`: `192.168.1.2`
  - `Laptop1`: `192.168.1.1`
- **Router1**:
  - Interface on Network 1: `10.1.1.3`
  - Interface on Network 2: `192.168.1.3`


## Detailed Packet Journey

### Initiating Ping Command
- **Command**: `ping 192.168.1.1` from `PC0`.
- **Packet**: ICMP Echo Request
  - Source IP: `10.1.1.1`
  - Destination IP: `192.168.1.1`

### Packet Routing and Forwarding

1. **PC0 checks its routing table** and forwards the packet to its default gateway, `Router1 (10.1.1.3)`.
2. **Router1 receives the packet** and checks its routing table.
3. **Router1 routes the packet** to its interface on Network 2 (`192.168.1.3`) and forwards it to `PC1`.

## Steps to Simulate ICMP Ping

1. **Initiate Ping Command**:
   - From `PC0`, open the command prompt and type `ping 192.168.1.1`.

2. **ICMP Echo Request Creation**:
   - `PC0` generates an ICMP Echo Request packet with:
     - Source IP: `10.1.1.1` (PC0’s IP)
     - Destination IP: `192.168.1.1` (PC1’s IP)

3. **Check Routing Table (PC0)**:
   - `PC0` checks its routing table and forwards the packet to its default gateway (`Router1`’s IP `10.1.1.3`).

4. **Forward Packet to Router1**:
   - `PC0` sends the ICMP Echo Request packet to `Router1` (`10.1.1.3`).

5. **Router1 Receives Packet**:
   - `Router1` receives the ICMP Echo Request packet on its interface `10.1.1.3` and examines the destination IP (`192.168.1.1`).

6. **Route the Packet (Router1)**:
   - `Router1` checks its routing table, routes the packet to its interface on Network 2 (`192.168.1.3`), and forwards it to `PC1`.

7. **Forward Packet to PC1**:
   - `Router1` forwards the ICMP Echo Request packet to `PC1` (`192.168.1.1`).

8. **PC1 Receives ICMP Echo Request**:
   - `PC1` processes the packet and generates an ICMP Echo Reply packet with:
     - Source IP: `192.168.1.1` (PC1’s IP)
     - Destination IP: `10.1.1.1` (PC0’s IP)

9. **Send Echo Reply to Router1**:
   - `PC1` sends the ICMP Echo Reply packet to its default gateway (`Router1`’s IP `192.168.1.3`).

10. **Router1 Receives Echo Reply**:
    - `Router1` receives the ICMP Echo Reply packet on its interface `192.168.1.3` and examines the destination IP (`10.1.1.1`).

11. **Route the Echo Reply**:
    - `Router1` checks its routing table, routes the packet to its interface on Network 1 (`10.1.1.3`), and forwards it to `PC0`.

12. **Forward Packet to PC0**:
    - `Router1` forwards the ICMP Echo Reply packet to `PC0` (`10.1.1.1`).

13. **PC0 Receives Echo Reply**:
    - `PC0` receives the ICMP Echo Reply packet, and the ping command completes successfully.


## Key Points

- **Routing**: The router’s role is crucial in determining the correct path for the packets.
- **Default Gateway**: Devices send packets to their default gateway if the destination is outside their local subnet.


