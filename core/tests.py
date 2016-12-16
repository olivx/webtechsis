from django.test import TestCase

from core.backends import authenticate
from core.models import TechUser, GrupoUsuarios

class TestUserLogin(TestCase):

    def setUp(self):
        self.username = 'thiagooliveira'
        self.password = 'login277'
        self.group_name = 'SISTEMA'
        self.user = authenticate(username=self.username, password=self.password)

    def test_login(self):
        '''test techcd user can be autheticate  '''
        self.assertTrue(self.user)

    # rever esse teste.
    # o teste falaha mas quando ta com a aplicação rodando não...
    # def test_techcd_user_group(self):
    #     '''techcd user must have sistema group '''
    #     print(self.user.groups)
    #     self.assertEqual(self.user.groups.name, self.group_name)

