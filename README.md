# ApexPlanet Cybersecurity Internship – Task 1

## Overview

This repository contains my work for Task 1 of the ApexPlanet Cybersecurity Internship.

The task focuses on building foundational knowledge in cybersecurity, networking, cryptography, Linux, and setting up an isolated cybersecurity lab environment.

## Objectives

- Understand the CIA Triad
- Learn common cybersecurity threats and attack vectors
- Set up a cybersecurity lab using VirtualBox
- Configure Kali Linux as the security testing machine
- Configure Metasploitable2 as an intentionally vulnerable target
- Configure an isolated Host-Only network
- Practice basic Linux commands
- Understand networking fundamentals
- Learn basic cryptography concepts
- Perform encryption and decryption using OpenSSL
- Capture and analyze network traffic using Wireshark
- Explore security tools including Nmap, Burp Suite, and Netcat

## Lab Environment

| Component | Purpose |
|---|---|
| Kali Linux | Security testing machine |
| Metasploitable2 | Intentionally vulnerable target |
| VirtualBox | Virtualization platform |
| Wireshark | Network traffic analysis |
| Nmap | Network discovery and service scanning |
| Burp Suite | Web application testing |
| Netcat | Network debugging and communication |
| OpenSSL | Cryptographic operations |

## Network Architecture

The lab is designed to use a **Host-Only Adapter** so that the vulnerable target remains within an isolated lab environment.

```text
Kali Linux
(Security Testing Machine)
       |
       | Host-Only Network
       |
Metasploitable2
(Intentionally Vulnerable Target)
