# OpenVAS Findings Summary – Metasploitable2

## 1. Assessment Overview

An OpenVAS vulnerability assessment was conducted against the intentionally vulnerable **Metasploitable2** virtual machine as part of the Network Security task.

The purpose of the assessment was to identify vulnerabilities, outdated software, insecure services, weak authentication mechanisms, and other security weaknesses.

| Parameter          | Details            |
| ------------------ | ------------------ |
| Target             | Metasploitable2    |
| Target IP          | `192.168.56.102`   |
| Scanner            | OpenVAS / GVM      |
| Scan Configuration | Full and fast      |
| Scan Status        | Completed          |
| Scan Date          | September 28, 2026 |

---

## 2. Vulnerability Summary

After applying the report filtering, the OpenVAS assessment identified **48 findings**:

| Severity  | Findings |
| --------- | -------: |
| Critical  |       10 |
| High      |        5 |
| Medium    |       30 |
| Low       |        3 |
| **Total** |   **48** |

The OpenVAS report contained 554 results before filtering. The final report included results meeting the configured Quality of Detection (QoD) threshold.

---

## 3. Key Findings

The assessment identified several significant security weaknesses.

### Critical Findings

* **TWiki vulnerabilities** on port `80/tcp`
* **Distributed Ruby (dRuby/DRb) RCE vulnerabilities** on port `8787/tcp`
* **MySQL weak authentication** on port `3306/tcp`
* **Ubuntu 8.04 end-of-life operating system**
* **VNC default password** on port `5900/tcp`
* **vsftpd 2.3.4 backdoor** on port `21/tcp`
* **Possible Ingreslock backdoor** on port `1524/tcp`
* **vsftpd backdoor shell** on port `6200/tcp`
* **rexec service** on port `512/tcp`
* **DistCC remote code execution vulnerability** on port `3632/tcp`

### High and Medium Findings

Other findings included:

* Vulnerable EasyPHP web server
* Anonymous FTP access
* FTP cleartext authentication
* Outdated jQuery
* TWiki CSRF vulnerability
* Additional vulnerabilities affecting lega
