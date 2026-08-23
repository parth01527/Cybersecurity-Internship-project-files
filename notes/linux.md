# Linux Basics

## 1. Introduction

Linux is an open-source operating system widely used in servers, networking, cloud computing, cybersecurity, and penetration testing.

Kali Linux is a Debian-based Linux distribution designed for cybersecurity testing, digital forensics, vulnerability assessment, and security research.

This section covers basic Linux commands related to file system navigation, file permissions, package management, and networking.

---

## 2. File System Navigation

Linux uses a hierarchical file system. The `/` directory is the root of the file system.

### pwd

The `pwd` command displays the current working directory.

```bash
pwd
```

Example output:

```text
/home/kali
```

### ls

The `ls` command lists files and directories in the current directory.

```bash
ls
```

Useful options:

```bash
ls -l
ls -a
ls -la
```

- `-l` displays detailed information.
- `-a` displays hidden files.
- `-la` displays detailed information including hidden files.

### cd

The `cd` command is used to change the current directory.

```bash
cd /tmp
```

Go back to the previous directory:

```bash
cd ..
```

Go to the home directory:

```bash
cd ~
```

---

## 3. File and Directory Permissions

Linux uses permissions to control who can read, write, or execute files and directories.

The three basic permissions are:

| Permission | Meaning |
|---|---|
| `r` | Read |
| `w` | Write |
| `x` | Execute |

Permissions are assigned to:

- **User (u)** — owner of the file
- **Group (g)** — group associated with the file
- **Others (o)** — all other users

Example:

```text
-rwxr-xr--
```

This represents permissions for the owner, group, and others.

### chmod

The `chmod` command changes file or directory permissions.

Example:

```bash
chmod 755 script.sh
```

This gives:

- Owner: read, write, execute
- Group: read, execute
- Others: read, execute

Another example:

```bash
chmod 644 file.txt
```

This gives:

- Owner: read, write
- Group: read
- Others: read

### chown

The `chown` command changes the owner and/or group of a file or directory.

Example:

```bash
sudo chown kali file.txt
```

To change both owner and group:

```bash
sudo chown kali:kali file.txt
```

---

## 4. Package Management

Kali Linux uses the Debian package management system.

### apt

`apt` is used to install, update, and remove software packages.

Update the package list:

```bash
sudo apt update
```

Upgrade installed packages:

```bash
sudo apt upgrade
```

Install a package:

```bash
sudo apt install <package-name>
```

Remove a package:

```bash
sudo apt remove <package-name>
```

Search for a package:

```bash
apt search <package-name>
```

### dpkg

`dpkg` is a lower-level Debian package management tool.

To install a `.deb` package:

```bash
sudo dpkg -i package.deb
```

To view installed packages:

```bash
dpkg -l
```

To check information about a package:

```bash
dpkg -s <package-name>
```

---

## 5. Networking Commands

Linux provides several commands for checking network configuration and connectivity.

### ifconfig

The `ifconfig` command displays network interface information.

```bash
ifconfig
```

It can show information such as:

- IP address
- Network interface
- MAC address
- Network statistics

Modern Linux systems commonly use the `ip` command instead.

Example:

```bash
ip addr
```

### ping

The `ping` command tests network connectivity between two hosts using ICMP.

Example:

```bash
ping 192.168.56.101
```

A successful response indicates that the target is reachable and responding to ICMP requests.

In the cybersecurity lab, Kali Linux can use `ping` to test connectivity with Metasploitable 2.

### netstat

The `netstat` command can display network connections, listening ports, and network statistics.

Example:

```bash
netstat -tuln
```

Common options:

- `-t` — TCP connections
- `-u` — UDP connections
- `-l` — listening ports
- `-n` — display numerical addresses and ports

On newer Linux systems, `ss` is commonly used as an alternative:

```bash
ss -tuln
```

### traceroute

The `traceroute` command displays the path packets take toward a destination.

Example:

```bash
traceroute 8.8.8.8
```

It can help identify the network hops between the source and destination.

If `traceroute` is not installed:

```bash
sudo apt install traceroute
```

---

## 6. Practical Lab Commands

The following commands can be used in the Kali Linux and Metasploitable 2 lab.

### Check Kali's IP address

```bash
ip addr
```

### Check Metasploitable 2's IP address

```bash
ifconfig
```

### Test connectivity

```bash
ping <Metasploitable-IP>
```

### Check listening network ports

```bash
netstat -tuln
```

### Trace a network route

```bash
traceroute <destination>
```

---

## 7. Summary

The Linux commands covered in this section provide basic skills required for navigating a Linux system, managing files and permissions, installing software, and troubleshooting network connectivity.

| Command | Purpose |
|---|---|
| `pwd` | Show current directory |
| `ls` | List files and directories |
| `cd` | Change directory |
| `chmod` | Change permissions |
| `chown` | Change ownership |
| `apt` | Manage packages |
| `dpkg` | Manage Debian packages |
| `ifconfig` | Display network configuration |
| `ip addr` | Display IP configuration |
| `ping` | Test network connectivity |
| `netstat` | Display network connections and ports |
| `traceroute` | Display the network path to a destination |

## Practical Evidence

Screenshots can be captured while executing these commands in Kali Linux to demonstrate practical understanding of Linux navigation, permissions, package management, and networking.
