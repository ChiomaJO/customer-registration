import unittest

from app import app, get_db


class CustomerRegistrationAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            get_db().execute('DELETE FROM customers')
            get_db().commit()

    def test_home_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Customer Registration', response.get_data(as_text=True))

    def test_home_page_links_to_customers_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('/customers', response.get_data(as_text=True))

    def test_valid_registration(self):
        payload = {
            'fullName': 'Jane Doe',
            'email': 'jane@example.com',
            'phone': '1234567890',
            'dateOfBirth': '2000-01-01',
            'gender': 'Female',
            'address': '123 Main St'
        }
        response = self.client.post('/register', data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Registration successful', response.get_json()['message'])

    def test_registration_is_saved_to_database(self):
        payload = {
            'fullName': 'John Smith',
            'email': 'john@example.com',
            'phone': '9876543210',
            'dateOfBirth': '1995-05-10',
            'gender': 'Male',
            'address': '456 Oak Ave'
        }
        self.client.post('/register', data=payload)

        with app.app_context():
            conn = get_db()
            row = conn.execute('SELECT full_name, email FROM customers WHERE email = ?', ('john@example.com',)).fetchone()
            self.assertIsNotNone(row)
            self.assertEqual(row['full_name'], 'John Smith')


if __name__ == '__main__':
    unittest.main()
