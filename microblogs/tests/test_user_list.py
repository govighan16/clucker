"""Unit tests of the user list."""
from django import forms
from django.contrib.auth.hashers import check_password
from django.test import TestCase
from microblogs.forms import SignUpForm
from microblogs.models import User


class SignUpFormTestCase(TestCase):
    """Unit tests of the user list."""

    def setUp(self):
        self.username = {
        'username':'@janedoe'
        }
        self.user_list = User.objects.all()

    def test_user_is_in_user_list(self):
        for self.username in self.user_list:
            self.assertEqual(self.username == "@janedoe")

    def test_user_not_is_in_user_list(self):
        if '@janedoe' in self.user_list:
            self.fail('Test should fail')

    def test_wrong_users_are_not_in_user_list(self):
        user_set = User.objects.filter(username="@johndoe")
        self.assertEqual(0, len(user_set))
