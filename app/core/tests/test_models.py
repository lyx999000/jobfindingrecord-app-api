from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user(self):
        """Testing creating a new user"""
        email = 'test@xxx.com'
        password = 'password'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_email_normalized(self):
        """Test the email for user is normalized"""
        email = 'test@CAPITAL.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password="test"
        )
        self.assertEqual(user.email,email.lower())
    
    def test_email_invalid(self):
        """Test create without email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
            None,
            "test"
        )

    def test_create_super_user(self):
        """Test creating super user"""
        user = get_user_model().objects.create_superuser(
            'super@test.com',
            'superuser'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)