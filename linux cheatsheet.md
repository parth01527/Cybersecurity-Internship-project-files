# Linux Cheat Sheet

A quick reference for commonly used Linux commands for cybersecurity labs and basic system administration.

---

## 1. File System Navigation

| Command | Purpose | Example |
|---|---|---|
| `pwd` | Show current directory | `pwd` |
| `ls` | List files and directories | `ls` |
| `ls -l` | Detailed file listing | `ls -l` |
| `ls -a` | Show hidden files | `ls -a` |
| `ls -la` | Detailed listing including hidden files | `ls -la` |
| `cd` | Change directory | `cd /tmp` |
| `cd ..` | Move to parent directory | `cd ..` |
| `cd ~` | Go to home directory | `cd ~` |
| `clear` | Clear terminal | `clear` |

---

## 2. File and Directory Management

| Command | Purpose | Example |
|---|---|---|
| `touch` | Create an empty file | `touch file.txt` |
| `mkdir` | Create a directory | `mkdir test` |
| `cp` | Copy a file/directory | `cp file.txt backup.txt` |
| `mv` | Move or rename a file | `mv old.txt new.txt` |
| `rm` | Remove a file | `rm file.txt` |
| `rmdir` | Remove an empty directory | `rmdir test` |
| `cat` | Display file contents | `cat file.txt` |
| `less` | View file contents page by page | `less file.txt` |
| `head` | Display beginning of a file | `head file.txt` |
| `tail` | Display end of a file | `tail file.txt` |

> Use `rm -r` carefully because it can remove directories and their contents.

---

## 3. File Permissions

Linux permissions consist of:

- `r` = Read
- `w` = Write
- `x` = Execute

Permissions apply to:

- `u` = User/Owner
- `g` = Group
- `o` = Others

### View permissions

```bash
ls -l
```

Example:

```text
-rwxr-xr--
```

### Change permissions

```bash
chmod 755 script.sh
```

Common permission values:

| Permission | Meaning |
|---|---|
| `400` | Owner read |
| `600` | Owner read/write |
| `644` | Owner read/write, others read |
| `700` | Owner read/write/execute |
| `755` | Owner full access, others read/execute |

### Change ownership

```bash
sudo chown user:user file.txt
```

Example:

```bash
sudo chown kali:kali file.txt
```

---

## 4. Package Management

Kali Linux uses Debian-based package management.

### Update package lists

```bash
sudo apt update
```

### Upgrade packages

```bash
sudo apt upgrade
```

### Install a package

```bash
sudo apt install <package-name>
```

### Remove a package

```bash
sudo apt remove <package-name>
```

### Search for a package

```bash
apt search <package-name>
```

### View installed packages

```bash
dpkg -l
```

### Install a `.deb` package

```bash
sudo dpkg -i package.deb
```

---

## 5. Networking Commands

### Display IP configuration

```bash
ip addr
```

or:

```bash
ifconfig
```

### Test connectivity

```bash
ping <IP-address>
```

Example:

```bash
ping 192.168.56.101
```

### Display network connections

```bash
netstat -tuln
```

Alternative:

```bash
ss -tuln
```

### Trace network route

```bash
traceroute <destination>
```

---

## 6. Important Network Information

| Item | Example |
|---|---|
| IP Address | `192.168.56.101` |
| MAC Address | `08:00:27:AB:CD:EF` |
| HTTP | Port `80` |
| HTTPS | Port `443` |
| SSH | Port `22` |
| FTP | Port `21` |
| DNS | Port `53` |
| RDP | Port `3389` |

---

## 7. Process Management

### Display running processes

```bash
ps
```

Detailed process list:

```bash
ps aux
```

### Display processes in real time

```bash
top
```

Alternative:

```bash
htop
```

### Terminate a process

```bash
kill <PID>
```

Force terminate:

```bash
kill -9 <PID>
```

---

## 8. User and Privilege Commands

### Display current username

```bash
whoami
```

### Display user ID and group information

```bash
id
```

### Display logged-in users

```bash
who
```

### Execute a command with administrative privileges

```bash
sudo <command>
```

Example:

```bash
sudo apt update
```

---

## 9. Search Commands

### Find a file

```bash
find /path -name "filename"
```

Example:

```bash
find /home -name "test.txt"
```

### Search inside files

```bash
grep "text" file.txt
```

Example:

```bash
grep "error" logfile.txt
```

### Locate a command

```bash
which nmap
```

Example:

```bash
which wireshark
```

---

## 10. System Information

### Display system information

```bash
uname -a
```

### Display hostname

```bash
hostname
```

### Display disk usage

```bash
df -h
```

### Display directory size

```bash
du -sh <directory>
```

### Display memory usage

```bash
free -h
```

---

## 11. File Viewing and Editing

### Display a file

```bash
cat file.txt
```

### Create a file

```bash
touch file.txt
```

### Edit a file using nano

```bash
nano file.txt
```

### View the first lines

```bash
head file.txt
```

### View the last lines

```bash
tail file.txt
```

---

## 12. Useful Cybersecurity Commands

### Check IP address

```bash
ip addr
```

### Test connectivity

```bash
ping <target-IP>
```

### Check listening ports

```bash
ss -tuln
```

### Check network connections

```bash
netstat -tuln
```

### Find Nmap location

```bash
which nmap
```

### Check Nmap version

```bash
nmap --version
```

### Check OpenSSL version

```bash
openssl version
```

---

## 13. Lab Commands

### Kali Linux

Check Kali's IP address:

```bash
ip addr
```

### Metasploitable 2

Check Metasploitable 2's IP address:

```bash
ifconfig
```

### Test Kali → Metasploitable connectivity

```bash
ping <Metasploitable-IP>
```

### Check listening ports

```bash
ss -tuln
```

---

## 14. File Permission Quick Reference

```text
r = Read
w = Write
x = Execute
```

Common numeric values:

```text
4 = Read
2 = Write
1 = Execute
```

Therefore:

```text
7 = Read + Write + Execute
6 = Read + Write
5 = Read + Execute
4 = Read
0 = No permission
```

Example:

```bash
chmod 755 script.sh
```

Means:

```text
Owner  → Read + Write + Execute
Group  → Read + Execute
Others → Read + Execute
```

---

## 15. Quick Command Reference

```text
pwd              Show current directory
ls               List files
ls -la            List all files with details
cd                Change directory
cd ..             Go to parent directory
mkdir             Create directory
touch             Create file
cp                Copy file
mv                Move/rename file
rm                Delete file
cat               Display file contents
nano              Edit file
chmod             Change permissions
chown             Change ownership
apt update        Update package lists
apt upgrade       Upgrade packages
apt install       Install package
dpkg -l           List installed packages
ip addr           Show IP configuration
ifconfig          Show network configuration
ping              Test connectivity
ss -tuln          Show listening ports
netstat -tuln     Show network connections
traceroute        Trace network path
ps aux            Show running processes
top               Monitor processes
kill              Terminate process
whoami            Show current user
id                Show user/group information
find              Find files
grep              Search text
uname -a          Show system information
df -h             Show disk usage
free -h           Show memory usage
```

---

## 16. Cybersecurity Lab Tools

Some commonly used cybersecurity tools available in Kali Linux include:

| Tool | Purpose |
|---|---|
| Wireshark | Network packet capture and analysis |
| Nmap | Network discovery and port scanning |
| Burp Suite | Web application security testing |
| Netcat | Network communication and troubleshooting |
| Metasploit | Security testing framework |
| OpenSSL | Cryptographic operations and TLS testing |

---

## Conclusion

This cheat sheet provides a quick reference for essential Linux commands used during cybersecurity labs. The commands cover file system navigation, file management, permissions, package management, networking, process management, system information, and basic security tools.
````
