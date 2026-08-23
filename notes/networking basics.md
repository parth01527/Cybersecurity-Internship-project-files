# Networking Basics

## 1. Introduction

Computer networking is the process of connecting computers, devices, and systems so that they can communicate and exchange data.

Networking is an important part of cybersecurity because security professionals need to understand how devices communicate, how network traffic is generated, and how attacks can affect networks.

In this task, a private virtual lab was created using Kali Linux as the testing machine and Metasploitable 2 as the target machine.

---

## 2. IP Address

An IP address is a logical address assigned to a device on a network. It is used to identify a device and allow communication between devices.

There are two commonly used versions of IP:

- IPv4
- IPv6

### IPv4

IPv4 uses 32-bit addresses and is normally written in four decimal sections.

Example:

```text
192.168.56.101
```

Each section can contain a value from 0 to 255.

### Private IP Addresses

Private IP addresses are used inside local networks and are not directly routable over the public Internet.

Common private IPv4 ranges include:

- `10.0.0.0/8`
- `172.16.0.0/12`
- `192.168.0.0/16`

The virtual cybersecurity lab uses a private network so that Kali Linux and Metasploitable 2 can communicate safely.

---

## 3. MAC Address

A MAC address is a hardware-level address associated with a network interface.

It is normally represented in hexadecimal format.

Example:

```text
08:00:27:AB:CD:EF
```

A MAC address is used for communication at the data-link layer of a network.

IP addresses identify devices logically, while MAC addresses identify network interfaces at the local network level.

---

## 4. TCP and UDP

TCP and UDP are transport-layer protocols used for communication between applications and systems.

### TCP

TCP stands for Transmission Control Protocol.

TCP is connection-oriented and provides reliable delivery of data.

Characteristics:

- Connection-oriented
- Reliable
- Provides ordered delivery
- Uses acknowledgements
- Performs retransmission when required

TCP is commonly used by protocols such as:

- HTTP
- HTTPS
- SSH
- FTP

### UDP

UDP stands for User Datagram Protocol.

UDP is connectionless and does not provide the same delivery guarantees as TCP.

Characteristics:

- Connectionless
- Faster and lightweight
- No guaranteed delivery
- No guaranteed ordering
- Lower overhead

UDP is commonly used by:

- DNS
- DHCP
- Streaming applications
- Real-time applications

### TCP vs UDP

| Feature | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented | Connectionless |
| Reliability | Reliable | No delivery guarantee |
| Ordering | Maintains order | No ordering guarantee |
| Speed | Generally slower | Generally faster |
| Overhead | Higher | Lower |
| Example | HTTPS, SSH | DNS, DHCP |

---

## 5. Common Network Protocols

### HTTP

HTTP stands for Hypertext Transfer Protocol.

It is used for communication between web browsers and web servers.

Default port:

```text
80
```

HTTP does not encrypt application data by itself.

### HTTPS

HTTPS stands for Hypertext Transfer Protocol Secure.

It uses TLS to protect communication between a client and a web server.

Default port:

```text
443
```

HTTPS provides encryption and helps protect the confidentiality and integrity of web traffic.

### DNS

DNS stands for Domain Name System.

DNS translates domain names into IP addresses.

Example:

```text
example.com → IP address
```

Common DNS port:

```text
53
```

DNS can use both UDP and TCP depending on the type of communication.

### DHCP

DHCP stands for Dynamic Host Configuration Protocol.

It automatically provides network configuration information to devices.

This can include:

- IP address
- Subnet mask
- Default gateway
- DNS server

Common ports:

```text
UDP 67 - Server
UDP 68 - Client
```

### FTP

FTP stands for File Transfer Protocol.

It is used to transfer files between systems.

Common port:

```text
21
```

FTP does not provide encryption by default, so secure alternatives such as SFTP are commonly preferred.

### SSH

SSH stands for Secure Shell.

It provides secure remote access to systems and can also be used for secure file transfer and tunneling.

Default port:

```text
22
```

---

## 6. Network Ports

A port is a logical communication endpoint used by applications and services.

Port numbers range from:

```text
0 - 65535
```

Some commonly encountered ports are:

| Port | Protocol/Service | Purpose |
|---|---|---|
| 21 | FTP | File transfer |
| 22 | SSH | Secure remote access |
| 23 | Telnet | Remote access |
| 25 | SMTP | Email transfer |
| 53 | DNS | Domain name resolution |
| 80 | HTTP | Web traffic |
| 110 | POP3 | Email retrieval |
| 143 | IMAP | Email retrieval |
| 443 | HTTPS | Secure web traffic |
| 3389 | RDP | Remote Desktop |

Understanding ports is important in cybersecurity because exposed or vulnerable services can increase the attack surface of a system.

---

## 7. Host-Only Network

A Host-Only Adapter in VirtualBox creates a private network that allows virtual machines and the host system to communicate without directly exposing the virtual machines to the external network.

For the cybersecurity lab:

```text
Kali Linux
    |
    | Private Network
    |
Metasploitable 2
```

This type of isolated environment is useful for security testing because the intentionally vulnerable target can be tested without exposing it unnecessarily to the public Internet.

---

## 8. Network Connectivity Testing

The `ping` command can be used to test whether one host can communicate with another host.

Example:

```bash
ping <Metasploitable-IP>
```

For example:

```bash
ping 192.168.56.101
```

A successful response can look similar to:

```text
64 bytes from 192.168.56.101: icmp_seq=1 ttl=64 time=0.5 ms
```

The response indicates that the target is reachable and responding to ICMP requests.

In the lab, Kali Linux was used to send ICMP echo requests to Metasploitable 2.

---

## 9. ICMP

ICMP stands for Internet Control Message Protocol.

It is used for network diagnostics and error reporting.

The `ping` command commonly uses ICMP:

```text
Kali Linux
    |
    | ICMP Echo Request
    ↓
Metasploitable 2
    |
    | ICMP Echo Reply
    ↓
Kali Linux
```

Wireshark can be used to observe these ICMP packets.

---

## 10. Basic Network Commands

### ip addr

Displays information about network interfaces and IP addresses.

```bash
ip addr
```

### ifconfig

Displays network interface configuration.

```bash
ifconfig
```

### ping

Tests connectivity between hosts.

```bash
ping <IP-address>
```

### netstat

Displays network connections and listening ports.

```bash
netstat -tuln
```

### traceroute

Shows the network path toward a destination.

```bash
traceroute <destination>
```

---

## 11. Wireshark

Wireshark is a network protocol analyzer used to capture and inspect network traffic.

It can display information about protocols such as:

- Ethernet
- ARP
- ICMP
- TCP
- UDP
- DNS
- HTTP

### Basic Wireshark Process

1. Open Wireshark.
2. Select the network interface used by the lab.
3. Start packet capture.
4. Generate network traffic.
5. Stop the capture when sufficient packets have been collected.
6. Apply a display filter to analyze specific traffic.

For example, the following filter displays ICMP traffic:

```text
icmp
```

During the lab, ICMP traffic generated by the Kali Linux to Metasploitable 2 ping test was captured using Wireshark.

---

## 12. Network Traffic Analysis

Network traffic contains information about communication between devices.

When analyzing traffic, security professionals can examine:

- Source IP address
- Destination IP address
- Source port
- Destination port
- Protocol
- Packet size
- TCP flags
- Packet contents when available

This information can help identify unusual communication, unauthorized services, suspicious connections, and potential security incidents.

---

## 13. Practical Lab Setup

The cybersecurity lab consists of two virtual machines:

### Kali Linux

Kali Linux is used as the testing and security assessment machine.

The IP address can be checked using:

```bash
ip addr
```

### Metasploitable 2

Metasploitable 2 is an intentionally vulnerable virtual machine designed for security testing and learning.

Its IP address can be checked using:

```bash
ifconfig
```

### Connectivity Test

Connectivity between the two machines was tested from Kali Linux using:

```bash
ping <Metasploitable-IP>
```

Successful ICMP replies confirmed network connectivity between the two virtual machines.

### Wireshark Capture

Wireshark was used to capture the network traffic generated during the ping test.

The following filter can be used to display the ICMP packets:

```text
icmp
```

---

## 14. Practical Observations

The lab demonstrated how two virtual machines can communicate over a private network.

The following observations were made:

1. Kali Linux received a private IP address.
2. Metasploitable 2 received a private IP address.
3. Both machines were connected to the same virtual network.
4. Kali Linux successfully sent ICMP requests to Metasploitable 2.
5. Metasploitable 2 responded with ICMP replies.
6. Wireshark captured and displayed the ICMP traffic.
7. Network information such as IP addresses and protocols could be observed in the captured packets.

---

## 15. Networking and Cybersecurity

Networking knowledge is essential for cybersecurity because many security attacks and defensive activities involve network communication.

Understanding IP addresses, ports, protocols, and packet structures helps security professionals:

- Identify exposed services
- Analyze suspicious network traffic
- Perform vulnerability assessments
- Investigate security incidents
- Configure firewalls
- Monitor network activity
- Detect unauthorized communication

Tools such as Wireshark and Nmap use networking concepts to help security professionals analyze and assess systems.

---

## 16. Summary

The main networking concepts covered in this section are:

| Concept | Description |
|---|---|
| IP Address | Logical address used to identify a device |
| MAC Address | Hardware-level address of a network interface |
| TCP | Reliable, connection-oriented transport protocol |
| UDP | Lightweight, connectionless transport protocol |
| HTTP | Web communication protocol |
| HTTPS | Secure web communication using TLS |
| DNS | Resolves domain names to IP addresses |
| DHCP | Automatically provides network configuration |
| FTP | File transfer protocol |
| SSH | Secure remote access protocol |
| Port | Logical endpoint used by applications |
| ICMP | Protocol used for diagnostics and network messages |
| Wireshark | Tool for capturing and analyzing network traffic |
| Host-Only Network | Private virtual network for isolated lab communication |

## Conclusion

Understanding networking fundamentals provides an important foundation for cybersecurity. The practical lab demonstrated communication between Kali Linux and Metasploitable 2 using a private virtual network. Connectivity was verified using ICMP ping, and the resulting network traffic was captured and analyzed using Wireshark.

This practical exercise helped demonstrate how IP addresses, protocols, ports, and packets work together during network communication.
