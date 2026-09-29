# ApexPlanet Cybersecurity Internship

This repository contains my practical work completed as part of the **ApexPlanet Cybersecurity Internship**.

The repository documents my cybersecurity learning and practical activities across multiple internship tasks, including cybersecurity fundamentals, lab setup, reconnaissance, network scanning, vulnerability assessment, packet analysis, and network security.

---

# Task 1 – Cybersecurity Fundamentals & Lab Setup

## Overview

This section contains my work for **Task 1 of the ApexPlanet Cybersecurity Internship**.

The task focused on building foundational knowledge in cybersecurity, networking, cryptography, Linux, and setting up an isolated cybersecurity lab environment.

## Objectives

* Understand the CIA Triad
* Learn common cybersecurity threats and attack vectors
* Set up a cybersecurity lab using VirtualBox
* Configure Kali Linux as the security testing machine
* Configure Metasploitable2 as an intentionally vulnerable target
* Configure an isolated Host-Only network
* Practice basic Linux commands
* Understand networking fundamentals
* Learn basic cryptography concepts
* Perform encryption and decryption using OpenSSL
* Capture and analyze network traffic using Wireshark
* Explore security tools including Nmap, Burp Suite, and Netcat

---

## Lab Environment

| Component       | Purpose                                |
| --------------- | -------------------------------------- |
| Kali Linux      | Security testing machine               |
| Metasploitable2 | Intentionally vulnerable target        |
| VirtualBox      | Virtualization platform                |
| Wireshark       | Network traffic analysis               |
| Nmap            | Network discovery and service scanning |
| Burp Suite      | Web application testing                |
| Netcat          | Network debugging and communication    |
| OpenSSL         | Cryptographic operations               |

---

## Network Architecture

The lab was designed using a **Host-Only Adapter** so that the intentionally vulnerable Metasploitable2 target remained isolated from external networks.

```text
              Isolated Host-Only Network
                       |
             +---------+---------+
             |                   |
        Kali Linux          Metasploitable2
     Security Testing      Vulnerable Target
          Machine
```

---

## CIA Triad

The CIA Triad was studied as a fundamental cybersecurity model.

### Confidentiality

Confidentiality ensures that sensitive information is accessible only to authorized users and systems.

### Integrity

Integrity ensures that information remains accurate and is not improperly modified or manipulated.

### Availability

Availability ensures that systems, services, and information remain accessible to authorized users when required.

---

## Common Cybersecurity Threats

The following cybersecurity threats and attack vectors were studied:

* Malware
* Phishing
* Password attacks
* Denial-of-Service attacks
* Man-in-the-Middle attacks
* Social engineering
* Web application attacks
* Network-based attacks

---

## Linux Fundamentals

Basic Linux commands and system administration concepts were practiced using Kali Linux.

Topics included:

* File and directory management
* File permissions
* Process management
* User management
* Networking commands
* Package management
* System information
* Basic shell operations

---

## Networking Fundamentals

The following networking concepts were studied:

* IP addressing
* MAC addresses
* TCP/IP
* TCP and UDP
* Ports and protocols
* DNS
* HTTP/HTTPS
* SSH
* FTP
* Network segmentation

---

## Cryptography

Basic cryptography concepts were studied using OpenSSL.

Practical activities included:

* Encryption
* Decryption
* Hashing
* Key generation
* Symmetric cryptography
* Asymmetric cryptography

---

## Network Traffic Analysis

Wireshark was introduced for capturing and analyzing network traffic.

The practical work included identifying:

* Source and destination IP addresses
* TCP and UDP communication
* Network protocols
* Packet headers
* Basic network traffic patterns

---

## Security Tools Explored

The following cybersecurity tools were explored during Task 1:

* Nmap
* Wireshark
* Burp Suite
* Netcat
* OpenSSL
* Kali Linux security utilities

---

# End of Task 1

The activities above completed the foundational cybersecurity concepts and isolated laboratory setup required for Task 1.

---

# Task 2 – Network Security Assessment

## Overview

This section contains my work for **Task 2 of the ApexPlanet Cybersecurity Internship**.

The task focused on **reconnaissance, network scanning, vulnerability assessment, packet analysis, and basic firewall configuration** using the isolated cybersecurity laboratory created during Task 1.

The practical assessment was performed using **Kali Linux** as the security testing machine and **Metasploitable2** as the intentionally vulnerable target.

---

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

---

## Lab Environment

| Component       | Purpose                                      |
| --------------- | -------------------------------------------- |
| Kali Linux      | Security testing and analysis machine        |
| Metasploitable2 | Intentionally vulnerable target              |
| VirtualBox      | Virtualization platform                      |
| Nmap            | Network discovery and port/service scanning  |
| OpenVAS         | Vulnerability assessment                     |
| Wireshark       | Network traffic capture and analysis         |
| iptables        | Firewall configuration and traffic filtering |

---

## Network Architecture

The assessment was conducted within an **isolated Host-Only network** created in VirtualBox.

This configuration prevents the intentionally vulnerable Metasploitable2 system from being exposed to external networks.

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

---

## 1. Reconnaissance

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

---

## 2. Nmap Network Scanning

Nmap was used to identify open ports, running services, service versions, and operating-system information.

### Scans Performed

* TCP SYN scan
* UDP scan
* Service/version detection
* OS detection
* Comprehensive scanning
* Banner grabbing

The complete Nmap scan outputs, commands, screenshots, and related files are available in the [`Nmap`](./Nmap) directory.

---

## 3. OpenVAS Vulnerability Assessment

OpenVAS was used to perform a vulnerability assessment against the Metasploitable2 target.

### Assessment Details

| Parameter          | Details            |
| ------------------ | ------------------ |
| Target             | Metasploitable2    |
| Target IP          | `192.168.56.102`   |
| Scanner            | OpenVAS / GVM      |
| Scan Configuration | Full and fast      |
| Scan Status        | Completed          |
| Scan Date          | September 28, 2026 |

### Vulnerability Summary

The filtered OpenVAS report identified:

| Severity  | Findings |
| --------- | -------: |
| Critical  |       10 |
| High      |        5 |
| Medium    |       30 |
| Low       |        3 |
| **Total** |   **48** |

The assessment identified vulnerabilities involving remote code execution, outdated software, weak/default credentials, backdoor services, insecure legacy protocols, and weak cryptographic configurations.

### OpenVAS Documentation

* [OpenVAS Scan Overview](./OpenVAS/openvas_scan_overview.md)
* [OpenVAS Findings Summary](./OpenVAS/openvas_findings_summary.md)
* [OpenVAS Vulnerability Report](./OpenVAS/openvas_report.pdf)

---

## 4. Wireshark Traffic Analysis

Wireshark was used to capture and analyze network traffic generated within the isolated lab.

The analysis covered:

* DNS traffic
* HTTP traffic
* FTP traffic
* Unencrypted FTP authentication
* SYN traffic associated with a simulated SYN flood

Detailed analysis, screenshots, and related files are available in the [`Wireshark`](./Wireshark) directory.

---

## 5. Firewall Configuration

Basic `iptables` rules were configured to demonstrate how network traffic can be allowed or blocked based on specific ports.

The firewall section documents:

* Firewall rule configuration
* Port blocking
* Verification using network scanning
* Before-and-after observations

---

## 6. Key Findings

The assessment demonstrated several important network-security concepts, including:

* Identification of exposed network services
* Service and version enumeration
* Vulnerability identification using OpenVAS
* Analysis of vulnerability severity
* Risks associated with unencrypted network protocols
* Identification of abnormal SYN traffic
* The role of firewall rules in reducing network exposure
* Importance of patching outdated software
* Importance of disabling unnecessary services
* Importance of
