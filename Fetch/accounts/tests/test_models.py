from django.db import IntegrityError
from accounts.factories import UserFactory
from accounts.models import User
from django.test import TestCase
from datetime import datetime


class ModelUserTest(TestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_email_user_verbose_name(self):
        user = User.object.get(id=self.user.id)
        field_verbose_name = user._meta.get_field('email').verbose_name
        self.assertEqual(field_verbose_name, 'email')

    def test_username_user_verbose_name(self):
        user = User.object.get(id=self.user.id)
        field_verbose_name = user._meta.get_field('username').verbose_name
        self.assertEqual(field_verbose_name, 'username')

    def test_date_joined_user_verbose_name(self):
        user = User.object.get(id=self.user.id)
        field_verbose_name = user._meta.get_field('date_joined').verbose_name
        self.assertEqual(field_verbose_name, 'date joined')

    def test_last_login_user_verbose_name(self):
        user = User.object.get(id=self.user.id)
        field_verbose_name = user._meta.get_field('last_login').verbose_name
        self.assertEqual(field_verbose_name, 'last login')

    def test_is_admin_user_verbose_name(self):
        user = User.object.get(id=self.user.id)
        field_verbose_name = user._meta.get_field('is_admin').verbose_name
        self.assertEqual(field_verbose_name, 'is admin')

    def test_is_active_user_verbose_name(self):
        user = User.object.get(id=self.user.id)
        field_verbose_name = user._meta.get_field('is_active').verbose_name
        self.assertEqual(field_verbose_name, 'is active')

    def test_is_staff_user_verbose_name(self):
        user = User.object.get(id=self.user.id)
        field_verbose_name = user._meta.get_field('is_staff').verbose_name
        self.assertEqual(field_verbose_name, 'is staff')

    def test_is_superuser_user_verbose_name(self):
        user = User.object.get(id=self.user.id)
        field_verbose_name = user._meta.get_field('is_superuser').verbose_name
        self.assertEqual(field_verbose_name, 'is superuser')

    def test_email_user_max_length(self):
        user = User.object.get(id=self.user.id)
        max_length = user._meta.get_field('email').max_length
        self.assertEqual(max_length, 60)

    def test_username_user_max_length(self):
        user = User.object.get(id=self.user.id)
        max_length = user._meta.get_field('email').max_length
        self.assertEqual(max_length, 60)

    def test_email_user_unique(self):
        with self.assertRaises(IntegrityError):
            user_1 = User.object.get(id=self.user.id)
            user_2 = User.object.create(
                email='test_user@gmail.com',
                username='test_user',
            )
            self.assertEqual(user_1.email, user_2.email)

    def test_username_user_unique(self):
        with self.assertRaises(IntegrityError):
            user_1 = User.object.get(id=self.user.id)
            user_2 = User.object.create(
                email='test_user@gmail.com',
                username='test_user',
            )
            self.assertEqual(user_1.username, user_2.username)

    def test_object_string_representation(self):
        user = User.object.get(id=self.user.id)
        expected_name = user.username
        self.assertEqual(str(user), expected_name)

    def test_date_joined_auto_now_add(self):
        user = User.object.get(id=self.user.id)
        self.assertIsInstance(user.date_joined, datetime)

    def test_last_login_auto_add(self):
        user = User.object.get(id=self.user.id)
        self.assertTrue(user.last_login)

    def test_is_admin_default_value(self):
        user = User.object.get(id=self.user.id)
        self.assertEqual(user.is_admin, False)

    def test_is_active_default_value(self):
        user = User.object.get(id=self.user.id)
        self.assertEqual(user.is_active, True)

    def test_is_staff_default_value(self):
        user = User.object.get(id=self.user.id)
        self.assertEqual(user.is_staff, True)

    def test_is_superuser_default_value(self):
        user = User.object.get(id=self.user.id)
        self.assertEqual(user.is_superuser, False)


class MyAccountManagerTest(TestCase):

    def setUp(self):
        self.test_user = User.object.create_user(
            email='test_user@gmail.com',
            username='test_user',
            password=''
        )
        self.test_superuser = User.object.create_superuser(
            email='test_superuser@gmail.com',
            username='test_superuser',
            password='',
        )

    def test_create_user(self):
        user = User.object.create_user(
            email='test_user_1@gmail.com',
            username='test_user_1',
            password=''
        )
        self.assertIsInstance(user, User)
        created_user = User.object.get(
            email='test_user_1@gmail.com',
            username='test_user_1',
        )
        self.assertEqual(user, created_user)

    def test_create_user_empty_email(self):
        with self.assertRaises(ValueError):
            User.object.create_user(
                email='',
                username='test_user',
                password=''
            )

    def test_create_user_empty_username(self):
        with self.assertRaises(ValueError):
            User.object.create_user(
                email='test_user@gmail.com',
                username='',
                password='',
            )

    def test_create_superuser(self):
        test_superuser = User.object.create_superuser(
            email='test_superuser_1@gmail.com',
            username='test_superuser_1',
            password='',
        )
        self.assertIsInstance(test_superuser, User)
        created_test_superuser = User.object.get(
            email='test_superuser_1@gmail.com',
            username='test_superuser_1',
        )
        self.assertEqual(test_superuser, created_test_superuser)

    def test_create_user_user_rank_admin(self):
        test_superuser = User.object.get(id=self.test_superuser.id)
        user_rank = test_superuser.is_admin
        self.assertEqual(user_rank, True)

    def test_create_user_user_rank_staff(self):
        test_superuser = User.object.get(id=self.test_superuser.id)
        user_rank = test_superuser.is_staff
        self.assertEqual(user_rank, True)

    def test_create_user_user_rank_superuser(self):
        test_superuser = User.object.get(id=self.test_superuser.id)
        user_rank = test_superuser.is_superuser
        self.assertEqual(user_rank, True)

    def test_create_superuser_empty_email(self):
        with self.assertRaises(ValueError):
            User.object.create_superuser(
                email='',
                username='test_superuser_1',
                password='Test_Superuser_1',
            )

    def test_create_superuser_empty_username(self):
        with self.assertRaises(ValueError):
            User.object.create_superuser(
                email='test_superuser_1@gmail.com',
                username='',
                password='Test_Superuser_1',
            )

    def test_create_user_normalize_email(self):
        User.object.create_user(
            email='ttest_user_1@GMAIL.com',
            username='testt',
            password='test'
        )
        created_user = User.object.get(
            username='testt',
        )
        self.assertEqual(created_user.email, 'ttest_user_1@gmail.com')
