# SQL Injection

## Objective

To demonstrate a SQL Injection vulnerability in DVWA and understand how an attacker can manipulate SQL queries to retrieve unauthorized database information.

## Lab Environment

* Application: Damn Vulnerable Web Application (DVWA)
* Security Level: Low
* Web Server: Apache
* Database: MariaDB
* Operating System: Kali Linux

## Vulnerability Demonstration

The DVWA SQL Injection module was tested using crafted input that altered the application's SQL query.

A UNION-based SQL Injection payload was used:

```text
1' UNION SELECT user,password FROM users#
```

The payload successfully caused the application to return usernames and password hashes from the database.

### Extracted Database Information

| Username | Password Hash                    |
| -------- | -------------------------------- |
| admin    | 5f4dcc3b5aa765d61d8327deb882cf99 |
| gordonb  | e99a18c428cb38d5f260853678922e03 |
| 1337     | 8d3533d75ae2c3966d7e0d4fcc69216b |
| pablo    | 0d107d09f5bbe40cade3de5c71e9e9b7 |
| smithy   | 5f4dcc3b5aa765d61d8327deb882cf99 |

## Impact

SQL Injection can allow an attacker to:

* Retrieve unauthorized database information.
* Bypass intended application logic.
* Access sensitive user information.
* Potentially modify or delete database records depending on database privileges.

## Mitigation – Prepared Statements

A separate PHP demonstration was created using a parameterized SQL query with a prepared statement.

The application used:

```php
$stmt = $conn->prepare(
    "SELECT first_name, last_name FROM users WHERE user_id = ?"
);

$stmt->bind_param("s", $id);
```

The normal request returned the expected user information, while the SQL Injection payload was treated as input rather than executable SQL syntax.

Additional output encoding was also applied using:

```php
htmlspecialchars()
```

## Result

The SQL Injection vulnerability was successfully demonstrated in the intentionally vulnerable DVWA environment, and the effectiveness of prepared statements as a mitigation was verified.

## Evidence

Screenshots demonstrating the SQL Injection attack, extracted database information, and prepared-statement mitigation are included in this folder.
