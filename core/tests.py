from datetime import datetime

from django.contrib.auth.models import User, Group
from django.core import mail
from django.shortcuts import resolve_url
from django.test import TestCase

from core.backends import authenticate
from core.form import ContactForm
from core.models import TechUser, GrupoUsuarios, Contact, PerennityLicense
from core.scripts import services


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


class TestViewContat(TestCase):

    def setUp(self):
        self.resp = self.client.get(resolve_url('contato'))

    def test_get(self):
        '''Test basic get '''
        self.assertEqual(200, self.resp.status_code)

    def test_template_in_used(self):
        '''Test if template in used is contato.html'''
        self.assertTemplateUsed(self.resp, 'contato.html')

    def test_contato_context(self):
        '''if has contato object in context'''
        context = self.resp.context['form']
        self.assertIsInstance(context, ContactForm)

class TestViewPost(TestCase):

    def setUp(self):
        data =  dict(nome='Thiago',categoria=Contact.SUGESTAO,
                     assunto='teste de envio assunto',menssagem='teste de envio messagens')
        self.resp = self.client.post(resolve_url('contato', ), data)


    def test_post(self):
        '''if ervery thing is ok, so thaks for that '''
        self.assertEqual(302, self.resp.status_code)

    def test_send_email(self):
        '''Test send mail'''
        self.assertEqual(len(mail.outbox), 1)


    def test_obejct_ceated(self):
        '''Test if contact is created on post '''
        self.assertTrue(Contact.objects.count(), 1)







































