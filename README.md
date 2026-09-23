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

# ApexPlanet Cybersecurity Internship – Task 2

## Overview

This repository contains my work for **Task 2 of the ApexPlanet Cybersecurity Internship**.

The task focuses on **reconnaissance, network scanning, vulnerability assessment, packet analysis, and basic firewall configuration** using an isolated cybersecurity lab environment.

The practical assessment was performed using **Kali Linux** as the security testing machine and **Metasploitable2** as the intentionally vulnerable target.

## Objectives

* Perform passive and active reconnaissance
* Identify hosts and services within the isolated lab environment
* Perform TCP and UDP port scanning using Nmap
* Identify running services and their versions
* Perform basic OS detection
* Generate and analyze Nmap scan results
* Perform vulnerability scanning using OpenVAS
* Analyze vulnerabilities based on severity
* Capture and analyze network traffic using Wireshark
* Analyze DNS, HTTP, and FTP traffic
* Demonstrate the security risks of unencrypted FTP traffic
* Analyze SYN traffic associated with a simulated SYN flood in the isolated lab
* Configure basic firewall rules using iptables
* Document findings and recommended security controls

## Lab Environment

| **Component**   | **Purpose**                                  |
| --------------- | -------------------------------------------- |
| Kali Linux      | Security testing and analysis machine        |
| Metasploitable2 | Intentionally vulnerable target              |
| VirtualBox      | Virtualization platform                      |
| Nmap            | Network discovery and port/service scanning  |
| OpenVAS         | Vulnerability assessment                     |
| Wireshark       | Network traffic capture and analysis         |
| iptables        | Firewall configuration and traffic filtering |

## Network Architecture

The assessment was conducted within an **isolated Host-Only network** created in VirtualBox. This prevents the intentionally vulnerable Metasploitable2 system from being exposed to external networks.

```text
              Isolated Host-Only Network
                       |
             +---------+---------+
             |                   |
        Kali Linux          Metasploitable2
     Security Testing      Vulnerable Target
          Machine
             |
       Nmap / OpenVAS
       Wireshark / iptables
```

## Reconnaissance

The reconnaissance phase involved identifying information about the target and understanding the available network services.

### Passive Reconnaissance

The following techniques were studied:

* WHOIS
* Nslookup
* Google Dorking
* Shodan

### Active Reconnaissance

The following techniques were performed within the isolated lab:

* Ping
* Host discovery
* Banner grabbing

## Nmap Scanning

Nmap was used to identify open ports, running services, service versions, and operating-system information.

### Scans Performed

* TCP SYN scan
* UDP scan
* Service/version detection
* OS detection

The complete scan outputs and analysis are available in the [`Nmap`](./Nmap/) directory.

## Vulnerability Assessment

OpenVAS was used to perform a vulnerability assessment against the Metasploitable2 target.

The assessment included:

* Vulnerability discovery
* Severity classification
* Affected services and ports
* Risk analysis
* Recommended remediation

The complete vulnerability report is available in the [`OpenVAS`](./OpenVAS/) directory.

## Wireshark Traffic Analysis

Wireshark was used to capture and analyze network traffic generated within the isolated lab.

The analysis covered:

* DNS traffic
* HTTP traffic
* FTP traffic
* Unencrypted FTP authentication
* SYN traffic associated with a simulated SYN flood

Detailed analysis and screenshots are available in the [`Wireshark`](./Wireshark/) directory.

## Firewall Configuration

Basic `iptables` rules were configured to demonstrate how network traffic can be allowed or blocked based on specific ports.

The firewall section documents:

* Firewall rule configuration
* Port blocking
* Verification using network scanning
* Before-and-after observations

## Key Findings

The assessment demonstrated several important network-security concepts, including:

* Identification of exposed network services
* Service and version enumeration
* Detection of vulnerabilities in an intentionally vulnerable system
* Risks associated with unencrypted network protocols
* Identification of abnormal SYN traffic
* The role of firewall rules in reducing network exposure

> **Note:** Specific findings and vulnerability details are documented based on the actual scan results obtained during the assessment.

## Reports

### Nmap Scan Report

The detailed Nmap scan report contains the commands used, scan results, observations, security implications, and recommendations.

### OpenVAS Vulnerability Report

The OpenVAS report contains the vulnerability findings, severity levels, affected services, analysis, and recommended remediation.

## Skills Demonstrated

* Network Reconnaissance
* Network Scanning
* Nmap
* OpenVAS
* Vulnerability Assessment
* Wireshark
* Packet Analysis
* TCP/IP Analysis
* FTP Security
* DNS Traffic Analysis
* Network Security
* Linux Firewall Configuration
* Security Documentation

## Ethical Use & Disclaimer

All scanning and security testing documented in this repository was performed against **systems intentionally configured for security testing within my isolated virtual lab environment**.

No unauthorized systems, networks, or third-party infrastructure were targeted.

This project is intended strictly for **educational and cybersecurity training purposes**.

