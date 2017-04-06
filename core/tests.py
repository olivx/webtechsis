from django.contrib.auth.models import User, Group
from django.test import TestCase

from core.backends import authenticate
from core.form import ContactForm
from core.models import TechUser, GrupoUsuarios, Contact


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

class TestModelContact(TestCase):

    def test_create_contact(self):
        '''Test if create  a fit object on database '''
        contatct =  Contact.objects.create(nome='thiago oliveira', categoria=Contact.SUGESTAO,
                                          assunto='teste de formulario', menssagem='Messangem teste')
        self.assertTrue(contatct)


class TestFormContact(TestCase):

    def test_form_is_valid(self):
        '''Form must be valid '''
        data  =  dict(nome='thiago oliveira', categoria=Contact.SUGESTAO,
                                          assunto='teste de formulario', menssagem='Messangem teste')
        form = ContactForm(data)
        self.assertTrue(form.is_valid())