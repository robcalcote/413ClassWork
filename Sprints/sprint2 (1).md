# Sprint 2: User Account

Sprint 2 is about your account app, user object, login and logout.

`version 1.0`

## Database

* Create DB in PostgreSQL
* Switch settings.py to use PostgreSQL

## User Model

* New `account` app, with models.py
* Custom user class (extends django.contrib.auth.models.AbstractUser)
* AUTH_USER_MODEL set to custom user class (in settings.py)
* makemigrations, migrate (set AUTH_USER_MODEL first!)

## Unit Tests

* Create fixtures file with users, groups, permissions
* Unit test to create a user, set data, save, then load again and compare.
* Unit test for login and logout
* Unit test for group permissions
* Unit test for users and groups
* Unit test for changing password

## Class Diagram

* auth_user
* auth_permission
* auth_group
* auth_group_permissions
* auth_user_groups
* auth_user_user_permissions
* django_content_type
* django_session
* django_migrations

## New app: `account`

* app_base.htm (inherits from /homepage/templates/base.htm)
* If logged out, /homepage/templates/base.htm shows "Login" link to /account/login/
* If logged in, /homepage/templates/base.htm shows "Account" dropdown with "Logout" link.

## /account/login/

* /account/views/login.py and /account/templates/login.html
* Django form
* `if request.method == 'POST'` logic
    * authenticate()
    * raise forms.ValidationError if authenticate fails
    * login() if authenticate succeeds
    * redirect to home page
* HTML template shows form
    * action is empty (same url)
    * method is POST

## /account/logout/

* /account/views/logout.py
* redirect to /account/login/
