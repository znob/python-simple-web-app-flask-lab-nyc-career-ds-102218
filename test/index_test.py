import unittest, sys
sys.path.insert(0, '..')
from hello_world import app


class HelloWorldTestCase(unittest.TestCase):
    testy = app.test_client()

    def test_index_status_code(self):
        response = self.testy.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_data(self):
        response = self.testy.get('/')
        raw = response.data
        result = raw.decode("utf-8")
        self.assertEqual(result, 'Hello, world!')

    def test_home_status_code(self):
        response = self.testy.get('/home')
        self.assertEqual(response.status_code, 200)

    def test_home_data(self):
        response = self.testy.get('/home')
        raw = response.data
        result = raw.decode("utf-8")
        self.assertEqual(result, 'Welcome to an amazing Flask App!')

    def test_myprofile_status_code(self):
        response = self.testy.get('/myprofile')
        self.assertEqual(response.status_code, 200)

    def test_myprofile_data(self):
        response = self.testy.get('/myprofile')
        raw = response.data
        result = raw.decode("utf-8")
        self.assertEqual(result, 'This is my profile! It\'s not finished yet... :/')

    def test_exit_status_code(self):
        response = self.testy.get('/exit')
        self.assertEqual(response.status_code, 200)

    def test_exit_data(self):
        response = self.testy.get('/exit')
        raw = response.data
        result = raw.decode("utf-8")
        self.assertEqual(result, 'Thanks for looking around. Come back again soon!')
