from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.test import TestCase

class TestBanckEndAutenticate(TestCase):

    def setUp(self):
        self.username = 'thiagooliveira'
        self.password = 'logan'
        self.group_name = 'SISTEMA'
        self.user = authenticate(username=self.username, password=self.password)

    def test_login(self):
        '''test techcd user can be autheticate  '''
        self.assertTrue(self.user)

    def test_erro_login(self):
        '''User cant login wif worn password '''
        password = 123456789
        user = authenticate(username=self.username, password=password)
        self.assertFalse(user)

    def test_group_is_system(self):
        '''The user group must be sistema '''
        group = Group.objects.filter(user__username=self.user.username).first()
        self.assertEqual('SISTEMAS', group.name )

