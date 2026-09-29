# OpenVAS Vulnerability Analysis – Metasploitable2

## 1. Scan Overview

An OpenVAS vulnerability assessment was performed against the intentionally vulnerable **Metasploitable2** virtual machine.

| Parameter          | Details            |
| ------------------ | ------------------ |
| Target             | Metasploitable2    |
| Target IP          | `192.168.56.102`   |
| Scanner            | OpenVAS            |
| Scan Configuration | Full and fast      |
| Scan Date          | September 28, 2026 |
| Scan Status        | Completed          |
| Scan Start         | 05:54:28 UTC       |
| Scan End           | 07:22:39 UTC       |

The purpose of the scan was to identify vulnerabilities, insecure services, outdated software, weak configurations, and other security weaknesses present on the Metasploitable2 system.

---

## 2. Vulnerability Summary

The OpenVAS report identified the following vulnerabilities after filtering:

| Severity  | Number of Findings |
| --------- | -----------------: |
| Critical  |                 10 |
| High      |                  5 |
| Medium    |                 30 |
| Low       |                  3 |
| **Total** |             **48** |

The report states that 48 results were selected by the report filtering, while 554 results were present before filtering. Results with a minimum Quality of Detection (QoD) of 70 were included in the report.

---

## 3. Critical Vulnerabilities

The scan identified 10 Critical findings.

| Port / Service | Vulnerability                                                  | CVSS |
| -------------- | -------------------------------------------------------------- | ---: |
| 80/tcp         | TWiki < 4.2.4 Multiple XSS / Command Execution Vulnerabilities | 10.0 |
| 8787/tcp       | Distributed Ruby (dRuby/DRb) Multiple RCE Vulnerabilities      | 10.0 |
| 3306/tcp       | MySQL security vulnerability / weak credentials                |  9.8 |
| General/TCP    | Ubuntu 8.04 End of Life                                        | 10.0 |
| 5900/tcp       | VNC Default Password                                           |  9.0 |
| 21/tcp         | vsftpd 2.3.4 Compromised Source Packages Backdoor              |  9.8 |
| 1524/tcp       | Possible Backdoor: Ingreslock                                  | 10.0 |
| 6200/tcp       | vsftpd Backdoor Shell                                          |  9.8 |
| 512/tcp        | rexec Service Running                                          | 10.0 |
| 3632/tcp       | DistCC Remote Code Execution Vulnerability                     |  9.3 |

### 3.1 TWiki < 4.2.4 Multiple XSS / Command Execution Vulnerabilities

**Port:** 80/tcp
**Severity:** Critical
**CVSS:** 10.0
**CVE:** CVE-2008-5304, CVE-2008-5305

The scan identified an outdated TWiki installation. The installed version was from February 2003, while version 4.2.4 is listed as the fixed version.

The vulnerability can allow execution of arbitrary script code or commands. It may also allow attackers to steal cookie-based authentication credentials or compromise the affected application.

**Recommended Remediation:** Upgrade TWiki to version 4.2.4 or later.

---

### 3.2 Distributed Ruby (dRuby/DRb) Multiple RCE Vulnerabilities

**Port:** 8787/tcp
**Severity:** Critical
**CVSS:** 10.0

The scan identified a Distributed Ruby service that could allow unauthorized systems to execute distributed commands.

The OpenVAS detection reported that arbitrary system-call commands could still be executed on the remote host.

**Recommended Remediation:** Disable the vulnerable service if it is not required or upgrade/configure the affected Ruby/Distributed Ruby implementation securely.

---

### 3.3 MySQL Security Issue

**Port:** 3306/tcp
**Severity:** Critical
**CVSS:** 9.8

The scan identified a serious MySQL authentication weakness. OpenVAS detected that the MySQL service allowed a root login with an empty password.

This configuration can allow unauthorized users to gain administrative access to the database.

**Recommended Remediation:** Set a strong password for database accounts, remove unnecessary accounts, disable remote administrative access where possible, and apply appropriate MySQL security hardening.

---

### 3.4 Ubuntu 8.04 End of Life

**Severity:** Critical
**CVSS:** 10.0

The operating system was identified as **Ubuntu 8.04**, which is an end-of-life release.

An unsupported operating system no longer receives normal security updates, leaving known vulnerabilities unpatched.

**Recommended Remediation:** Upgrade the operating system to a currently supported release.

---

### 3.5 VNC Default Password

**Port:** 5900/tcp
**Severity:** Critical
**CVSS:** 9.0

OpenVAS identified a VNC service using a default password.

Default credentials can allow unauthorized users to access the graphical desktop environment.

**Recommended Remediation:** Change the default VNC password, use strong authentication, restrict VNC access to trusted networks, and disable the service when it is not required.

---

### 3.6 vsftpd 2.3.4 Backdoor

**Port:** 21/tcp
**Severity:** Critical
**CVSS:** 9.8
**CVE:** CVE-2011-2523

The scan identified a compromised version of vsftpd 2.3.4 containing a backdoor.

The vulnerability can allow an attacker to obtain unauthorized shell access to the system.

**Recommended Remediation:** Remove the compromised version and install a trusted, patched version of the FTP service. If FTP is unnecessary, disable it.

---

### 3.7 Possible Ingreslock Backdoor

**Port:** 1524/tcp
**Severity:** Critical
**CVSS:** 10.0

OpenVAS identified a possible backdoor service on port 1524.

A backdoor can provide an attacker with unauthorized access and the ability to execute commands on the affected system.

**Recommended Remediation:** Disable and remove the unauthorized service and investigate the system for signs of compromise.

---

### 3.8 vsftpd Backdoor Shell

**Port:** 6200/tcp
**Severity:** Critical
**CVSS:** 9.8
**CVE:** CVE-2011-2523

OpenVAS identified a shell associated with the vulnerable vsftpd 2.3.4 backdoor.

The service can provide unauthorized shell access to the system.

**Recommended Remediation:** Remove the vulnerable vsftpd installation, install a trusted patched version, and disable unnecessary FTP services.

---

### 3.9 rexec Service Running

**Port:** 512/tcp
**Severity:** Critical
**CVSS:** 10.0
**CVE:** CVE-1999-0618

The rexec service was detected running on the target system.

rexec transmits authentication information without adequate encryption, which can expose usernames and passwords to interception.

**Recommended Remediation:** Disable rexec and use SSH for secure remote administration.

---

### 3.10 DistCC Remote Code Execution Vulnerability

**Port:** 3632/tcp
**Severity:** Critical
**CVSS:** 9.3
**CVE:** CVE-2004-2687

OpenVAS detected a vulnerable DistCC service.

The active check was able to execute the `id` command remotely and returned:

`uid=1(daemon) gid=1(daemon)`

This demonstrates that the vulnerable service could allow remote command execution.

**Recommended Remediation:** Disable DistCC if it is not required or upgrade it to a secure version and restrict access to trusted hosts.

---

## 4. High Severity Vulnerabilities

The scan identified 5 High severity findings.

Important findings included:

* **EasyPHP Webserver <= 12.1 Multiple Vulnerabilities** on port 80/tcp with a CVSS score of 7.5.
* Additional High severity findings were identified on ports **21/tcp** and **514/tcp**.

The EasyPHP finding was associated with the URL:

`http://192.168.56.102/phpinfo.php`

The vulnerability may expose sensitive information and may potentially allow further compromise depending on the vulnerable configuration.

**Recommended Remediation:** Upgrade or remove vulnerable software, disable unnecessary services, and restrict access to exposed administrative or information-disclosure endpoints.

---

## 5. Medium Severity Vulnerabilities

The scan identified 30 Medium severity findings.

Examples include:

### Anonymous FTP Login

**Port:** 21/tcp

OpenVAS detected anonymous FTP access using accounts such as:

`anonymous:anonymous@example.com`

Anonymous FTP can expose files to unauthorized users and may also allow unauthorized file operations depending on the server configuration.

**Recommended Remediation:** Disable anonymous FTP access unless it is specifically required.

### FTP Cleartext Authentication

**Port:** 21/tcp

FTP authentication can transmit login credentials without encryption.

**Recommended Remediation:** Use secure alternatives such as SFTP or FTPS and avoid transmitting credentials over unencrypted connections.

### jQuery XSS Vulnerability

**Port:** 80/tcp
**CVE:** CVE-2012-6708

The scan detected an outdated jQuery version:

`1.3.2`

The report identifies version 1.9.0 as the fixed version.

**Recommended Remediation:** Upgrade jQuery to a supported and secure version.

### TWiki CSRF Vulnerability

**Port:** 80/tcp

The scan identified a Cross-Site Request Forgery vulnerability in the outdated TWiki installation.

**Recommended Remediation:** Upgrade TWiki to a fixed version and apply appropriate web application security controls.

---

## 6. Low Severity Vulnerabilities

The scan identified 3 Low severity findings.

### Weak SSH MAC Algorithms

**Port:** 22/tcp
**CVSS:** 2.6

OpenVAS identified weak SSH MAC algorithms including:

* `hmac-md5`
* `hmac-md5-96`
* `hmac-sha1-96`
* `umac-64@openssh.com`

**Recommended Remediation:** Disable weak MAC algorithms and allow stronger cryptographic algorithms.

### SSL/TLS DHE_EXPORT / LogJam

**Port:** 25/tcp
**CVSS:** 3.7
**CVE:** CVE-2015-4000

The service was found to accept export-grade DHE cipher suites.

This can allow a man-in-the-middle attacker to downgrade a TLS session to weaker 512-bit export-grade cryptography.

**Recommended Remediation:** Disable DHE_EXPORT cipher suites and use modern, secure TLS configurations.

---

## 7. Overall Security Analysis

The OpenVAS scan demonstrates that the Metasploitable2 system contains multiple serious security weaknesses.

The most significant issues include:

* Outdated operating system and software.
* Remote code execution vulnerabilities.
* Backdoor services.
* Default and weak cre
