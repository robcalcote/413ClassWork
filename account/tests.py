from django.test import TestCase
from account import models as amod
from datetime import datetime

class UserTests(TestCase):
    fixtures = [ 'account.yaml' ]

    # TEST - get a user object; test the first name.
    def test_user_get(self):
        u1 = amod.User.objects.get(id=1)
        self.assertEqual(u1.first_name, 'Homer', msg="Name should have been 'Homer'")

    # TEST - create a user, set data, save, load again and compare.
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


class LoginNew(TestCase):
    fixtures = [ 'account.yaml' ]

    # TEST - create a new user and login
    def setUpNew(self):
        self.bob = amod.User()
        self.bob.username = 'bobross'
        self.bob.set_password('password123')
        self.bob.first_name = 'Bob'
        self.bob.last_name = 'Ross'
        self.bob.birth_date = datetime(1980, 1, 1)
        self.bob.favorite_color = 'Steel Blue'
        self.bob.save()
    def test_user_login(self):
        credentials = {
            'username': 'bobross',
            'password': 'password123'
        }
        response = self.client.post('/account/login/', credentials)
        request = response.wsgi_request
        self.assertTrue(request.user.is_authenticated, msg="User should have authenticated")
        self.assertEqual(request.user.id, self.bob.id, msg="User should have been bob")
        self.assertEqual(response.status_code, 302, msg="User wasn't redirected")
    
class LoginExisting(TestCase):
    fixtures = [ 'account.yaml' ]
    
    #Test - login existing user
    def setUpExisting(self):
        self.rob = amod.User.get(username='robcalcote')
        self.rob.set_password('testing123')
        self.rob.save()
    def test_user_login(self):
        credentials = {
            'username': 'robcalcote',
            'password': 'testing123'
        }
        response = self.client.post('/account/login/', credentials)
        request = response.wsgi_request
        self.assertTrue(request.user.is_authenticated, msg="User should have authenticated")
        self.assertEqual(request.user.id, self.rob.id, msg="User should have been robcalcote")
        self.assertEqual(response.status_code, 302, msg="User wasn't redirected")

