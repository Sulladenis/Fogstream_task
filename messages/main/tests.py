from django.test import TestCase
from django.urls import reverse

class TestCalls(TestCase):

    def test_call_view_denies_anonymous(self):
        response = self.client.get('/main/', follow=True)
        self.assertRedirects(response, '/main/login/?next=/main/')
        response = self.client.post('/main/', follow=True)
        self.assertRedirects(response, '/main/login/?next=/main/')

class GreetingViewResponseTests(TestCase):
    url = '/main/login/'
    template_name = 'main/login.html'


    def test_url_name(self):
        name_url = reverse('main:login')
        self.assertURLEqual(self.url, name_url)

    def test_page_response_code(self):     
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
    
    def test_page_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, self.template_name)

    def test_page_content(self):
        response = self.client.get(self.url)
        text = 'Регистрация'
        self.assertContains(response, text, status_code=200)