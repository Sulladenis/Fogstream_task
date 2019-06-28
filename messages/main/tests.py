from django.test import TestCase


class TestCalls(TestCase):

    def test_call_view_denies_anonymous(self):
        response = self.client.get('/main/', follow=True)
        self.assertRedirects(response, '/main/login/?next=/main/')
        response = self.client.post('/main/', follow=True)
        self.assertRedirects(response, '/main/login/?next=/main/')
    