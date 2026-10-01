# ApexPlanet Cybersecurity Internship – Task 3

## Web Application Security

This task focuses on identifying, exploiting, and mitigating common web application security vulnerabilities in a controlled laboratory environment using Damn Vulnerable Web Application (DVWA).

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

* Identifying common web application vulnerabilities.
* Understanding how vulnerable input handling can be exploited.
* Using Burp Suite for HTTP request analysis.
* Understanding SQL Injection and prepared statements.
* Understanding Stored and Reflected XSS.
* Implementing CSP and output encoding.
* Understanding CSRF and token-based protection.
* Identifying LFI and RFI vulnerabilities.
* Configuring and verifying HTTP security headers.
* Documenting security testing results with screenshots.

---

## Evidence

Each section contains its corresponding screenshots, testing results, and mitigation notes.

This task was performed entirely in a co
