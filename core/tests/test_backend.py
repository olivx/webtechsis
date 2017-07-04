from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, User
from django.test import TestCase
from model_mommy import mommy
from core.backends import TechCDBackend
from core.models import TechUser, GrupoUsuarios
from random import randint

class TestBanckEndAutenticate(TestCase):
    def setUp(self):
        self.username = 'thiagooliveira'
        self.password = 'logan'
        self.group_name = 'SISTEMA'
        self.grupo = GrupoUsuarios.objects.using('techcd').create(cod_grupo=1, desc_grupo='SISTEMA')
        self.user = TechUser.objects.using('techcd').create(cod_grupo=self.grupo,
                                                username='thiagooliveira',
                                                password='logan')

        self.user_auth = authenticate(username=self.username, password="logan")
        self.techcd = TechCDBackend()

    def tearDown(self):
        self.grupo.delete()
        self.user.delete()

    def test_login(self):
        """test techcd user can be autheticate  """
        self.assertTrue(self.user_auth)

    def test_erro_login(self):
        """User cant login wif worn password """
        password = 123456789
        user = authenticate(username=self.username, password='')
        self.assertFalse(user)

    def test_group_is_system(self):
        """The user group must be sistema """
        group = Group.objects.filter(user__username=self.user.username).first()
        self.assertEqual('SISTEMA', group.name)

    def test_return_user(self):
        """Test if  user exist , return user """
        self.assertIsInstance(self.user_auth, User)

    def test_get_user_not_none(self):
        """if id exists return user """
        self.assertTrue(self.techcd.get_user)

    def test_get_user_is_none(self):
        """if id not exists return user """
        self.assertFalse(self.techcd.get_user(2))

    def test_authenticate(self):
        user = self.techcd.authenticate(username='thiagooliveira', password='logan')
        self.assertTrue(user)






