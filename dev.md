# Concursus, Developer Documentation

## Endpoints

- `/admin/ensure-conn`: Ensures that connections can be made to our database
- `/admin/make-tables`: Creates the SQL tables that will store all our data
- `/admin/drop-tables`: Drops all data in our SQL tables
- `/admin/all-users`: Fetches all users' usernames and email ids.
> [!CAUTION]
> Remove the /drop-tables endpoint before shipping to prod.
- `/auth/register`: Register a user (POST request, user data in request body as json data.)

## Tables
### Users
The users table holds data about all the users.
Passwords are stored through the following processes:

```
+----------------+
| bcrypt.saltgen |
+----------------+
    ||
    VV
 +------+     +----------+     +----------------+  hashlib.scrypt   +-----------------+  Into DB
 | Salt |  ,  | Password |  ,  | Hashing Params |  ==============>  | Hashed password |  =======>
 +------+     +----------+     +----------------+                   +-----------------+
 29 chars                                                              64 long binary   
```

Fields:
1. `user_id` - MEDIUMINT(8)
2. `email` - VARCHAR(255)
3. `username` - VARCHAR(50)
4. `password` - BINARY(64)
5. `salt` - CHAR(29)
6. `created_at` - TIMESTAMP
7. `bio` - TEXT

> [!NOTE]
> Should emails also be hashed?
> What other fields should be added to the user table? (See [Issue #1](https://github.com/concursus-app/concursus/issues/1))
