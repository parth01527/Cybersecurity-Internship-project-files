# Burp Suite Advanced

## Objective

To use Burp Suite to intercept, inspect, modify, and fuzz HTTP requests against the DVWA web application in a controlled local environment.

## Lab Environment

* Application: Damn Vulnerable Web Application (DVWA)
* Security Level: Low
* Tool: Burp Suite
* Operating System: Kali Linux

## 1. HTTP Request Interception

Burp Suite Proxy was used to intercept HTTP traffic between the browser and the DVWA application.

The Burp Suite built-in browser was used to access the DVWA login page, and the login request was captured through:

**Proxy → Intercept**

The request was inspected before being forwarded to the application.

## 2. Request Modification

The captured login request was sent to Burp Suite for further testing.

A request parameter was modified before sending the request to the DVWA server.

For example, the username parameter was changed from:

```text
admin
```

to:

```text
testuser
```

The modified request was then sent and the resulting server response was observed.

This demonstrated how an intercepted HTTP request can be inspecte
