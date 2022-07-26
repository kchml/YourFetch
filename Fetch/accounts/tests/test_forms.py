from django.test import TestCase
from accounts.forms import CreateUserForm, LoginForm
from accounts.models import User


class Test_LoginForm(TestCase):

    def setUp(self):
        self.test_user = CreateUserForm(data={
            'username': 'test',
            'email': 'test@gmail.com',
            'password1': 'Test1234#56789',
            'password2': 'Test1234#56789',
        })

    def test_LoginForm_email_field_label(self):
        form = LoginForm()
        self.assertTrue(
            form.fields['email'].label is None or
            form.fields['email'].label == 'email'
        )

    def test_LoginForm_password_field_label(self):
        form = LoginForm()
        self.assertTrue(
            form.fields['password'].label is None or
            form.fields['password'].label == 'password'
        )

    def test_form_is_valid(self):
        form = self.test_user
        self.assertTrue(form.is_valid())


class Test_CreateUserForm(TestCase):

    def setUp(self):
        self.test_user = CreateUserForm(data={
            'username': 'test',
            'email': 'test@gmail.com',
            'password1': 'Test1234#56789',
            'password2': 'Test1234#56789',
        })

    def test_CreateUserForm_model_label(self):
        form = CreateUserForm().Meta()
        self.assertEqual(form.model, User)

    def test_CreateUserForm_fields(self):
        form = self.test_user
        self.assertIn('username', form.fields)
        self.assertIn('email', form.fields)
        self.assertIn('password1', form.fields)
        self.assertIn('password2', form.fields)
