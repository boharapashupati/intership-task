# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth.models import User
# from rest_framework.test import APITestCase, APIClient
# from rest_framework import status
# from .models import ExpenseIncome

# # Create your tests here.

# class ExpenseIncomeAPITestCase(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='user1', password='pass1234')
#         self.superuser = User.objects.create_superuser(username='admin', password='adminpass')
#         self.login_url = reverse('token_obtain_pair')
#         self.refresh_url = reverse('token_refresh')
#         self.register_url = reverse('register')
#         self.expenses_url = '/api/expenses/'
#         self.client = APIClient()

#     def authenticate(self, username, password):
#         response = self.client.post(self.login_url, {'username': username, 'password': password})
#         self.assertEqual(response.status_code, 200)
#         token = response.data['access']
#         self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

#     def test_user_registration(self):
#         response = self.client.post(self.register_url, {'username': 'newuser', 'password': 'newpass123'})
#         self.assertEqual(response.status_code, 201)
#         self.assertIn('message', response.data)

#     def test_login_with_valid_and_invalid_credentials(self):
#         # Valid
#         response = self.client.post(self.login_url, {'username': 'user1', 'password': 'pass1234'})
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('access', response.data)
#         # Invalid
#         response = self.client.post(self.login_url, {'username': 'user1', 'password': 'wrong'})
#         self.assertEqual(response.status_code, 401)

#     def test_token_refresh(self):
#         response = self.client.post(self.login_url, {'username': 'user1', 'password': 'pass1234'})
#         refresh = response.data['refresh']
#         response = self.client.post(self.refresh_url, {'refresh': refresh})
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('access', response.data)

#     def test_crud_operations(self):
#         self.authenticate('user1', 'pass1234')
#         # Create
#         data = {
#             'title': 'Test Expense',
#             'description': 'Test Desc',
#             'amount': 100,
#             'transaction_type': 'debit',
#             'tax': 10,
#             'tax_type': 'flat'
#         }
#         response = self.client.post(self.expenses_url, data)
#         self.assertEqual(response.status_code, 201)
#         expense_id = response.data['id']
#         # List
#         response = self.client.get(self.expenses_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data['count'], 1)
#         # Retrieve
#         response = self.client.get(f'{self.expenses_url}{expense_id}/')
#         self.assertEqual(response.status_code, 200)
#         # Update
#         response = self.client.put(f'{self.expenses_url}{expense_id}/', {**data, 'title': 'Updated'})
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data['title'], 'Updated')
#         # Delete
#         response = self.client.delete(f'{self.expenses_url}{expense_id}/')
#         self.assertEqual(response.status_code, 204)

#     def test_permission_regular_user(self):
#         self.authenticate('user1', 'pass1234')
#         # Create an expense
#         data = {
#             'title': 'User1 Expense',
#             'amount': 50,
#             'transaction_type': 'debit',
#             'tax': 5,
#             'tax_type': 'flat'
#         }
#         response = self.client.post(self.expenses_url, data)
#         expense_id = response.data['id']
#         # Try to access as another user
#         self.client.credentials()  # Remove auth
#         self.authenticate('admin', 'adminpass')
#         response = self.client.get(f'{self.expenses_url}{expense_id}/')
#         self.assertEqual(response.status_code, 200)  # Superuser can access
#         # Regular user cannot access another user's record
#         self.client.credentials()  # Remove auth
#         user2 = User.objects.create_user(username='user2', password='pass5678')
#         self.authenticate('user2', 'pass5678')
#         response = self.client.get(f'{self.expenses_url}{expense_id}/')
#         self.assertEqual(response.status_code, 404)

#     def test_business_logic_tax_calculation(self):
#         self.authenticate('user1', 'pass1234')
#         # Flat tax
#         data = {
#             'title': 'Flat Tax',
#             'amount': 100,
#             'transaction_type': 'debit',
#             'tax': 10,
#             'tax_type': 'flat'
#         }
#         response = self.client.post(self.expenses_url, data)
#         self.assertEqual(response.data['total'], 110)
#         # Percentage tax
#         data['tax_type'] = 'percentage'
#         response = self.client.post(self.expenses_url, data)
#         self.assertEqual(response.data['total'], 110)
#         # Zero tax
#         data['tax'] = 0
#         response = self.client.post(self.expenses_url, data)
#         self.assertEqual(response.data['total'], 100)

#     def test_unauthenticated_requests(self):
#         response = self.client.get(self.expenses_url)
#         self.assertEqual(response.status_code, 401)
#         response = self.client.post(self.expenses_url, {})
#         self.assertEqual(response.status_code, 401)
