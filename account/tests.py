from django.test import TestCase
from account import models as amod

class AccountTests(TestCase):
    fixtures = [ 'account.yaml' ]

    def test_user_get(self):
        u1 = amod.User.objects.get(id=1)
        # We are testing that the user with id=1 has the first name Homer
        self.assertEqual(u1.first_name, 'Homer', msg="Name should have been 'Homer'")

    def test_user_create(self):
        u = amod.User()
        u.username = 'harrypotter'
        u.first_name = 'Harry'
        u.last_name = 'Potter'
        u.set_password('password123')
        u.is_superuser = False
        u.email = 'harry@potter.com'
        u.favorite_color = 'black'
        u.save()
        u4 = amod.User.objects.get(id=4)
        self.assertEqual(u.first_name, u4.first_name, msg="Name should have been 'Harry'")

class LoginTests(TestCase):
    fixtures = [ '' ]

class GroupPermissions(TestCase):
    fixtures = [ '' ]

