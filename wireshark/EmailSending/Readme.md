# Capturing and Analyzing Email Packets with Wireshark

This guide provides a step-by-step walkthrough on how to capture and analyze network packets while sending an email using Gmail. We will use Wireshark, a powerful network protocol analyzer, to capture the packets and examine the communication process.

## Prerequisites

- A computer with an internet connection.
- Wireshark installed. You can download it from [Wireshark's official website](https://www.wireshark.org/download.html).

## Steps to Capture Packets

### 1. Open Wireshark

1. Launch Wireshark on your computer.
2. You will see a list of available network interfaces.

### 2. Select Network Interface

1. Choose the network interface that you are using to connect to the internet (e.g., Wi-Fi or Ethernet).
2. Click on the interface to start capturing packets.

### 3. Start Packet Capture

1. Click the blue shark fin icon at the top left to start capturing packets.

### 4. Send an Email

1. Open your email client (e.g., Gmail via a web browser).
2. Compose a new email and send it to any recipient.

### 5. Stop Packet Capture

1. Return to Wireshark.
2. Click the red square icon at the top left to stop capturing packets.

## Analyzing the Captured Packets

### 1. Apply Filters

1. To focus on the relevant packets, apply the `ssl` filter:
   - Type `ssl` in the filter bar and press Enter.

### 2. Understanding the Captured Packets

#### Overview of Captured Packets

- **Source IP**: The IP address of your device.
- **Destination IP**: The IP address of the Gmail server.
- **Protocol**: `TLSv1.2` indicating encrypted communication using TLS version 1.2.
- **Info**: Additional information about the packet.

#### Detailed Breakdown

1. **Packet List (Top Pane)**:
   - Each row represents a single packet.
   - Key columns include:
     - **No.**: Packet number.
     - **Time**: Timestamp of when the packet was captured.
     - **Source**: The IP address of the sender (your device).
     - **Destination**: The IP address of the receiver (Gmail server).
     - **Protocol**: Protocol used, in this case, `TLSv1.2`.
     - **Length**: Size of the packet.
     - **Info**: Additional details about the packet.

2. **Highlighted Packet**:
   - Select a packet to see its detailed breakdown.
   - Example: Packet number 1.
   - **Source IP**: Your device's IP (e.g., 192.168.0.6).
   - **Destination IP**: Gmail server's IP (e.g., 163.70.145.13).
   - **Protocol**: `TLSv1.2`.

3. **Packet Details (Middle Pane)**:
   - Detailed breakdown of the selected packet.
   - **Ethernet II**: Hardware addresses of the source and destination.
   - **Internet Protocol Version 4**: IP addresses and packet identification details.
   - **Transmission Control Protocol (TCP)**: TCP segment details, including flags and sequence numbers.
   - **Transport Layer Security (TLS)**: Encrypted application data.

4. **Packet Bytes (Bottom Pane)**:
   - Raw data of the packet in hexadecimal and ASCII formats.

### 3. Types of Packets

1. **DNS Packets**:
   - Resolve the Gmail server’s IP address.
   - Filter: `dns`.

2. **TCP Handshake**:
   - Establish connection with the Gmail server.
   - Packets: `SYN`, `SYN-ACK`, `ACK`.

3. **TLS Handshake**:
   - Secure the communication.
   - Packets: `Client Hello`, `Server Hello`.

4. **Encrypted Application Data**:
   - Actual email content sent as encrypted data.
   - Filter: `tls`.

### Example Analysis

1. **Packet 1**:
   - **Source**: Your device.
   - **Destination**: Gmail server.
   - **Protocol**: `TLSv1.2`.
   - **Info**: Encrypted application data.

2. **Details of Packet 1**:
   - **Ethernet II**: Physical layer information.
   - **IPv4**: IP addresses and packet length.
   - **TCP**: TCP flags and segment information.
   - **TLS**: Encrypted application data.

## Summary

- **DNS Resolution**: Your device resolves the Gmail server's IP address.
- **TCP Handshake**: Establishes a connection with the server.
- **TLS Handshake**: Secures the communication.
- **Encrypted Communication**: Email content is sent as encrypted data using TLS.

By following these steps and using Wireshark, you can capture and analyze the packets involved in sending an email through Gmail. The packets will show encrypted communication, ensuring the privacy and security of your email data.

---

This README provides a detailed guide on capturing and analyzing email packets using Wireshark, with explanations tailored to the information visible in the above provided screenshot.

