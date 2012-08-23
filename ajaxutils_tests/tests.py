from django.test import TestCase
from django.contrib.auth.models import User

from ajaxutils import json


class TestAjaxDecorator(TestCase):
    def setUp(self):
        User.objects.create_superuser('chuck', 'chuck@example.com', 'norris')

    def test_simple(self):
        response = self.client.get('/simple/')
        self.assertEqual(response.status_code, 200)

        json.loads(response.content)

    def test_simple_get_success(self):
        response = self.client.get('/simple_bool_get/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/simple_get/')
        self.assertEqual(response.status_code, 200)

        json.loads(response.content)

    def test_simple_get_failure(self):
        response = self.client.post('/simple_bool_get/')
        self.assertEqual(response.status_code, 405)

        response = self.client.post('/simple_get/')
        self.assertEqual(response.status_code, 405)

        json.loads(response.content)

    def test_simple_post_success(self):
        response = self.client.post('/simple_bool_post/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/simple_post/')
        self.assertEqual(response.status_code, 200)

        json.loads(response.content)

    def test_simple_post_failure(self):
        response = self.client.get('/simple_bool_post/')
        self.assertEqual(response.status_code, 405)

        response = self.client.get('/simple_post/')
        self.assertEqual(response.status_code, 405)

        json.loads(response.content)

    def test_logged_success(self):
        self.client.login(username='chuck', password='norris')
        response = self.client.get('/logged/')
        self.assertEqual(response.status_code, 200)

        json.loads(response.content)

    def test_logged_failure(self):
        response = self.client.get('/logged/')
        self.assertEqual(response.status_code, 401)

        json.loads(response.content)

    def test_catch_http_404_exception(self):
        response = self.client.get('/raise/404/')
        self.assertEqual(response.status_code, 404)

        json.loads(response.content)

    def test_custom_status_code(self):
        response = self.client.get('/custom/712/')
        self.assertEqual(response.status_code, 712)

        json.loads(response.content)

    def test_methods_argument_allows_given_methods(self):
        response = self.client.get('/simple_get_and_post/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/simple_get_and_post/')
        self.assertEqual(response.status_code, 200)

        json.loads(response.content)

    def test_methods_argument_denies_blocked_methods(self):
        response = self.client.delete('/simple_get_and_post/')
        self.assertEqual(response.status_code, 405)

        response = self.client.put('/simple_get_and_post/')
        self.assertEqual(response.status_code, 405)

        json.loads(response.content)
