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
| S. No. | Fieldname | Datatype |
| --------------- | --------------- | --------------- |
| 1 | `user_id` | `MEDIUMINT(8) PRIMARY KEY` |
| 2 | `email` | `VARCHAR(255)` |
| 3 | `username` | `VARCHAR(50)` |
| 4 | `password` | `BINARY(64)` |
| 5 | `salt` | `CHAR(29)` |
| 6 | `created_at` | `TIMESTAMP` |
| 7 | `bio` | `TEXT` |
| 8 | `muns_attended` | `INT`? |
| 9 | `best_delegates_won` | `INT`? |
| 10 | `outstanding_delegates_won` | `INT`? |
| 11 | `commendable_delegates_won` | `INT`? |
| 12 | `special_mentions_won` | `INT`? |
| 13 | `fav_portfolio_1` | `VARCHAR(25)` |
| 14 | `fav_committee_1` | `VARCHAR(25)` |
| 15 | `fav_portfolio_2` | `VARCHAR(25)` |
| 16 | `fav_committee_2` | `VARCHAR(25)` |
| 17 | `fav_portfolio_3` | `VARCHAR(25)` |
| 18 | `fav_committee_3` | `VARCHAR(25)` |
| 19 | `fav_portfolio_4` | `VARCHAR(25)` |
| 20 | `fav_committee_4` | `VARCHAR(25)` |
| 21 | `points` | `INT`? |
| 22 | `institution_delegation` | `FOREIGN KEY TO DELEGATION TABLE` |
| 23 | `private_delegation` | `FOREIGN KEY TO DELEGATION TABLE` |

> [!NOTE]
> Should emails also be hashed?

> [!NOTE]
> What other fields should be added to the user table? (See [Issue #1](https://github.com/concursus-app/concursus/issues/1))

### MUNs
> [!NOTE]
> This table is yet to be implemented

Fields:
| S. No. | Fieldname | Datatype | 
| --------------- | --------------- | --------------- |
| 1 | `mun_id` | `MEDIUMINT(8) PRIMARY KEY` |
| 2 | `name` | `VARCHAR(50)` |
| 3 | `organizers` | (Many-to-Many relation)? |
| 4 | `bio` | `TEXT` |
| 5 | `website` | `TEXT`? |
| 6 | `committees` | `FOREIGN KEY TO COMMITTEES TABLE` |
| 7 | `registered_users` | (Many-to-Many relation)? |
| 8 | `registered_delegations` | (Many-to-Many relation)? |
| 9 | `icon` | (Imgur link)? |
| 10 | `banner` | (Imgur link)? |
| 11 | `reg_fee` | `INT NULLABLE`? |
| 12 | `best_delegate_prize` | `INT NULLABLE`? |
| 13 | `outstanding_delegate_prize` | `INT NULLABLE`? |
| 14 | `commendable_delegate_prize` | `INT NULLABLE`? |
| 15 | `start_date` | `DATE`? |
| 16 | `end_date` | `DATE`? |

MUNs will stay in the database unless deleted, even after their completion. 
This property will be used to map users and the MUNs they have attended.

### Committees
> [!NOTE]
> This table is yet to be implemented

Fields:
| S. No. | Fieldname | Datatype |
| --------------- | --------------- | --------------- |
| 1 | `committee_id` | `MEDIUMINT(8) PRIMARY KEY` |
| 2 | `is_default` | `BOOL` |
| 3 | `default_id` | `FOREIGN KEY TO DEFAULT COMMITTEES TABLE` |
| 4 | `agenda` | `VARCHAR(100)` |
| 5 | `about_agenda` | `TEXT` |
| 6 | `name` | `VARCHAR(20) NULLABLE` |
| 7 | `about_committee` | `TEXT NULLABLE` |
| 8 | `chair_1` | `FOREGIN KEY TO USERS TABLE` |
| 9 | `chair_2` | `FOREGIN KEY TO USERS TABLE NULLABLE` |
| 10 | `chair_3` | `FOREGIN KEY TO USERS TABLE NULLABLE` |
| 11 | `matrix` | (Google sheets link)? |
| 12 | `background_guide` | (Google drive link)? |
| 13 | `icon` | (Imgur link, NULLABLE)? |
| 14 | `marksheet` | (Google sheets link)? |
| 15 | `is_public` | `BOOL` |
| 16 | `delegates` | (Many-to-Many relation)? |

> [!IMPORTANT]
> How do we track allotments?

### Delegations

Fields:
| S. No. | Fieldname | Datatype |
| --------------- | --------------- | --------------- |
| 1 | `name` | `VARCHAR(20)` |
| 2 | `admins` | (Many-to-Many relation)? |
| 3 | `delegates` | (Many-to-Many relation)? |
| 4 | `applications` | (Many-to-Many relation)? |
| 5 | `best_delegations_won` | `INT`? |



