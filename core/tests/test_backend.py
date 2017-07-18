from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, User
from django.test import TestCase
from core.backends import TechCDBackend
from core.models import TechUser, GrupoUsuarios

class TestBanckEndAutenticate(TestCase):

    def _setUp(self):

        self.username = 'thiagooliveira'
        self.password = 'logan'
        self.group_name = 'SISTEMA'
        self.grupo = GrupoUsuarios.objects.create(cod_grupo=1, desc_grupo='SISTEMA')
        self.user = TechUser.objects.create(cod_grupo=self.grupo,
                                                username='thiagooliveira',
                                                password='logan')

        self.user_auth = authenticate(username=self.username, password="logan")
        self.techcd = TechCDBackend()

    def _tearDown(self):
        self.grupo.delete()
        self.user.delete()

    def _test_login(self):
        """test techcd user can be autheticate  """
        self.assertTrue(self.user_auth)

    def _test_erro_login(self):
        """User cant login wif worn password """
        password = 123456789
        user = authenticate(username=self.username, password='')
        self.assertFalse(user)

    def _test_group_is_system(self):
        """The user group must be sistema """
        group = Group.objects.filter(user__username=self.user.username).first()
        self.assertEqual('SISTEMA', group.name)

    def _test_return_user(self):
        """Test if  user exist , return user """
        self.assertIsInstance(self.user_auth, User)

    def _test_get_user_not_none(self):
        """if id exists return user """
        self.assertTrue(self.techcd.get_user)

    def _test_get_user_is_none(self):
        """if id not exists return user """
        self.assertFalse(self.techcd.get_user(2))

    # def test_authenticate(self):
    #     user = self.techcd.authenticate(username='thiagooliveira', password='logan')
    #     self.assertTrue(user)






