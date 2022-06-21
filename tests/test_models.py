from rest_framework.test import APITestCase
from authentication.models import User


class TestModels(APITestCase):

    def test_create_user(self):
        user = User.objects.create_user('Test username', 'test@test.com', 'teSt123_@')
        self.assertIsInstance(user, User)
        self.assertEquals(user.username, 'Test username')
        self.assertEquals(user.email, 'test@test.com')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_raise_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username='', email='test@test.com', password='teSt123@')

    def test_raise_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='', email='test@test.com', password='teSt123_@')

    def test_raise_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username='Test username', email='', password='teSt123@')

    def test_raise_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(username='Test username', email='', password='teSt123_@')

    def test_create_super_user(self):
        user = User.objects.create_superuser('Test username', 'test@test.com', 'teSt123_@')
        self.assertIsInstance(user, User)
        self.assertEquals(user.username, 'Test username')
        self.assertEquals(user.email, 'test@test.com')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_cant_create_super_user_with_no_is_staff_status(self):
        # todo check why this is not throwing an error
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True'):
            User.objects.create_superuser(
                username='Test_username', email='test@test.com', password='teSt123_@', is_staff=False)

    def test_cant_create_super_user_with_no_is_super_user_status(self):
        # todo check why this is not throwing an error
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True'):
            User.objects.create_superuser(
                username='Test_username', email='test@test.com', password='teSt123_@', is_superuser=False)

