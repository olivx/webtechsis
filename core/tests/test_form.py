from django.test import TestCase
from core.form import ContactForm
from core.models import Contact


class TestFormContact(TestCase):

    def _test_form_is_valid(self):
        '''Form must be valid '''
        data  =  dict(nome='thiago oliveira', categoria=Contact.SUGESTAO,
                                          assunto='teste de formulario', menssagem='Messangem teste')
        form = ContactForm(data)
        self.assertTrue(form.is_valid())