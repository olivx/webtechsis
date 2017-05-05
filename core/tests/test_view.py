from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url

from core.models import Contact
from core.form import ContactForm


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



