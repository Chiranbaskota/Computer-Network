# Cisco Packet Tracer Network Simulation - DHCP Automatic IP Assignment

## Overview

This project demonstrates a basic network setup using Cisco Packet Tracer where DHCP is used to automatically assign IP addresses to devices in a single subnet. The network consists of a router, a switch, a server, and multiple PCs, all connected within the same subnet.

## Network Components

- **Router (Cisco 1841)**
  - Interface: `FastEthernet0/0`
  - IP Address: `10.0.0.1`
  - Function: Acts as the default gateway for the network and possibly the DHCP server.

- **Switch (Cisco 2960-24TT)**
  - Function: Connects all devices in the network, allowing for communication between them.

- **Server (Server0)**
  - IP Address: `10.0.0.10`
  - Function: May serve as the DHCP server or another role such as file hosting.

- **PCs**
  - **PC0**: `10.0.0.11`
  - **PC1**: `10.0.0.12`
  - **PC2**: `10.0.0.13`
  - **PC3**: `10.0.0.14`
  - **PC4**: `10.0.0.15`
  - Function: End devices in the network that receive IP addresses via DHCP.

## Network Configuration

### DHCP Server Configuration
The DHCP server (either the router or Server0) is configured to automatically assign IP addresses to the devices on the network within the `10.0.0.0/24` subnet.

### IP Addressing
- Subnet: `10.0.0.0/24`
- Gateway: `10.0.0.1`
- IP Range: `10.0.0.11 - 10.0.0.15`

### Steps to Setup
1. **Router Configuration:**
   - Configure the router interface `FastEthernet0/0` with the IP address `10.0.0.1`.
   - Enable DHCP service on the router if it is being used as the DHCP server.
   
2. **Switch Configuration:**
   - No specific configuration is required as it simply acts as a Layer 2 device connecting all PCs and the server.
   
3. **Server Configuration:**
   - If Server0 is acting as the DHCP server, configure it to assign IP addresses within the range `10.0.0.11 - 10.0.0.15`.

4. **PC Configuration:**
   - Set each PC to automatically obtain an IP address via DHCP.

### Simulation
- Run the simulation to observe the DHCP Discover, Offer, Request, and Acknowledge process.
- Ensure all PCs successfully receive an IP address and can communicate with each other.

## Conclusion

This network setup demonstrates how DHCP can be used to automate IP address assignment in a simple, single-subnet environment. It is an essential tool for managing IP addresses in any network, reducing the need for manual configuration and minimizing the risk of IP conflicts.


