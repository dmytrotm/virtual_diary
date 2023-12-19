import unittest
from website import create_app, db

class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000"

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF protection for testing
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def test_unauthorized_access(self):
        response = self.client.get('/start-page')
        self.assertEqual(response.status_code, 404)
        self.assertNotIn('Location', response.headers)

    def test_register_user(self):
        data = {
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'firstName': 'testuser'
        }
        response = self.client.post('/sign-up', data=data)
        self.assertEqual(response.status_code, 200)

    def test_register_duplicate_user(self):  # Fix the method name
        data = {
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'firstName': 'testuser'
        }
        response = self.client.post('/sign-up', data=data)
        self.assertEqual(response.status_code, 302)

    def test_login_logout_user(self):
        data = {
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        self.client.post('/register', json=data)
        login_response = self.client.post('/login', json=data)
        self.assertEqual(login_response.status_code, 200)

    def test_modify_user(self):
        # Register a user
        data = {
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'firstName': 'testuser'
        }
        self.client.post('/sign-up', data=data)

        # Log in the user
        login_data = {
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        self.client.post('/login', data=login_data)

        # Modify the user
        modify_data = {
            'email': 'unique3@example.com',
            'firstName': 'modifieduser',
            'password': 'newpassword'
        }

        response = self.client.post('/user', data=modify_data)
        self.assertEqual(response.status_code, 302)

    def test_delete_user(self):
        # Register a user
        data = {
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'firstName': 'testuser'
        }
        self.client.post('/sign-up', data=data)

        # Log in the user
        login_data = {
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        self.client.post('/login', data=login_data)

        # Delete the user
        response = self.client.delete('/user')
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()
