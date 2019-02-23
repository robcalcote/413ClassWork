# Sprint 2: User Account

Sprint 2 is about your account app, user object, login and logout.

`version 1.0`

-----------------------------
#X# Database
-----------------------------
#X# Create DB in PostgreSQL
#X# Switch settings.py to use PostgreSQL

-----------------------------
# # User Model
-----------------------------
# # New `account` app, with models.py
# # Custom user class (extends django.contrib.auth.models.AbstractUser)
# # AUTH_USER_MODEL set to custom user class (in settings.py)
# # makemigrations, migrate (set AUTH_USER_MODEL first!)

-----------------------------
# # Unit Tests
-----------------------------
# # Create fixtures file with users, groups, permissions
# # Unit test to create a user, set data, save, then load again and compare.
# # Unit test for login and logout
# # Unit test for group permissions
# # Unit test for users and groups
# # Unit test for changing password

-----------------------------
#X# Class Diagram
-----------------------------
#X# auth_user
#X# auth_permission
#X# auth_group
#X# auth_group_permissions
#X# auth_user_groups
#X# auth_user_user_permissions
#X# django_content_type
#X# django_session
#X# django_migrations

-----------------------------
# #  New app: `account`
-----------------------------
# # app_base.htm (inherits from /homepage/templates/base.htm)
# # If logged out, /homepage/templates/base.htm shows "Login" link to /account/login/
# # If logged in, /homepage/templates/base.htm shows "Account" dropdown with "Logout" link.

-----------------------------
# #  /account/login/
-----------------------------
# # /account/views/login.py and /account/templates/login.html
# # Django form
# # `if request.method == 'POST'` logic
# #    authenticate()
# #    raise forms.ValidationError if authenticate fails
# #    login() if authenticate succeeds
# #    redirect to home page
# # HT  template shows form
# #    action is empty (same url)
# #    method is POST

-----------------------------
# #  /account/logout/
-----------------------------
# # /account/views/logout.py
# # redirect to /account/login/
