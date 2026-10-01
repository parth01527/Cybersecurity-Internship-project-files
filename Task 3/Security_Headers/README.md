# Web Security Headers

## Objective

To analyze HTTP security headers and configure security headers on the local Apache web server hosting DVWA.

## 1. Security Headers Analysis

A public test website was analyzed using SecurityHeaders.com to understand how HTTP security headers are evaluated.

The scan was used to identify the presence or absence of common security headers and review the resulting security assessment.

## 2. Apache Security Header Configuration

Apache's `mod_headers` module was enabled:

```bash
sudo a2enmod headers
```

A dedicated Apache configuration file was created at:

```text
/etc/apache2/conf-available/security-headers.conf
```

The following security headers were configured:

```apache
<IfModule mod_headers.c>
    Header always set X-Content-Type-Options "nosniff"
    Header always set X-Frame-Options "SAMEORIGIN"
    Header always set Referrer-Policy "strict-origin-when-cross-origin"
    Header always set Permissions-Policy "geolocation=(), microphone=(), camera=()"
</IfModule>
```

The configuration was enabled using:

```bash
sudo a2enconf security-headers
```

The Apache configuration was then tested:

```bash
sudo apache2ctl configtest
```

The result was:

```text
Syntax OK
```

Apache was restarted after the configuration was enabled.

## 3. Verification

The configured headers were verified using:

```bash
curl -I http://127.0.0.1/dvwa/
```

The response contained:

```text
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: geolocation=(), microphone=(), camera=()
```

This confirmed that the security headers were being returned by the Apache server.

## Purpose of the Headers

### X-Content-Type-Options

`nosniff` helps prevent browsers from MIME-sniffing responses and interpreting content as a different type than declared.

### X-Frame-Options

`SAMEORIGIN` restricts framing of the application to pages from the same origin and can help reduce clickjacking risk.

### Referrer-Policy

`strict-origin-when-cross-origin` controls the amount of referrer information sent with requests, particularly across different origins.

### Permissions-Policy

The configured policy restricts access to selected browser features such as geolocation, microphone, and camera.

## Result

HTTP security headers were successfully configured in Apache and verified through an HTTP response from the local DVWA application.

## Evidence

Screenshots in this folder demonstrate:

1. SecurityHeaders.com analysis of the public test website.
2. Apache configuration and verification of the configured HTTP security headers.
