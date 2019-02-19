from django.test import TestCase
from account import models as amod

class AccounTests(TestCase):
    fixtures = [ 'account.yaml' ]

    def test_user_get(self):
        u1 = amod.User.objects.get(id=1)
        # BAD - usually never print things in a test if it works
        # While developing tests, it's ok, just don't keep it after
        # print('>>>>', u1.first_name)

        # Another wrong way:
        # if u1.first_name != 'Homer':
            # print('Nope. Bad first name')

        # We are testing that the user with id=1 has the first name Homer
        self.assertEqual(u1.first_name, 'Hom2er', msg="Name should have been 'Homer'")

    def test_user_create(self):
        u = amod.User()
        u.first_name = 'Harry'
        u.last_name = 'Potter'
        u........
        u.save()
        u2 = aomd.User.objects.get(u.id)
        self.assertEqual(u.first_name, u2.first_name, msg="...")