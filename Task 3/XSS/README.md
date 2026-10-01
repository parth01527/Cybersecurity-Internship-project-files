# Cross-Site Scripting (XSS)

## Objective

To demonstrate Stored and Reflected Cross-Site Scripting vulnerabilities in DVWA and implement mitigation using input validation and Content Security Policy (CSP).

## Lab Environment

* Application: Damn Vulnerable Web Application (DVWA)
* Security Level: Low
* Web Server: Apache
* Operating System: Kali Linux

## 1. Stored XSS

The DVWA Stored XSS module was tested by submitting a JavaScript payload through the application's input fields.

Payload used:

```html
<script>alert('XSS Test')</script>
```

The payload was stored by the application and executed when the affected content was displayed.

### Impact

Stored XSS can allow malicious JavaScript to execute in the browsers of users who view the affected content. Depending on the application, this can lead to session-related attacks, malicious page modification, phishing, or unauthorized actions performed in the victim's browser.

## 2. Reflected XSS

The DVWA Reflected XSS module was tested using a JavaScript payload supplied through the request parameter.

Payload used:

```html
<script>alert('Reflected XSS')</script>
```

The application reflected the supplied input into the response without sufficient output encoding, causing the JavaScript to execute.

### Impact

Reflected XSS can occur when attacker-controlled input is immediately reflected into a web response without proper sanitization or output encod
