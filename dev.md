# Concursus, Developer Documentation

## Endpoints

`/ensure-conn` (admin-only): Ensures that connections can be made to our database
`/make-tables` (admin-only): Creates the SQL tables that will store all our data

## Tables
### Users
The users table holds data about all the users.
Passwords are stored through the following processes:

```
+----------+     +------+       +-----------------+  MD5 Hashing  +------+  Into the DB
| Password |  +  | Salt |  ===> | Salted Password |  ===========> | Hash |  ===========>
+----------+     +------+       +-----------------+               +------+
```

Fields:
1. `user_id`
2. `email`
3. `username`
4. `password`
5. `salt`
6. `created_at`
7. `bio`

> [!NOTE]
> Should emails also be hashed?
> What other fields should be added to the user table?

