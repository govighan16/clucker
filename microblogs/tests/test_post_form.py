"""Unit tests of the post form."""
from django import forms
from django.contrib.auth.hashers import check_password
from django.test import TestCase
from microblogs.forms import PostForm
from microblogs.models import User


class SignUpFormTestCase(TestCase):
    """Unit tests of the post form."""

    def setUp(self):
        self.form_input = {'text' : 'This is a post text'}



    def test_valid_post_form(self):
        form = PostForm(data= self.form_input)
        self.assertTrue(form.is_valid())


    def test_form_has_necessary_fields(self):
        form = PostForm(data = self.form_input)
        self.assertIn('text', form.fields)
        #self.assertTrue(isinstance(email_field, forms.EmailField))

    def test_form_text_has_max_280_characters(self):
        form = PostForm(data = self.form_input)
        self.form_input['text'] = 'x' * 280
        self.assertTrue(form.is_valid())

    def test_form_text_must_not_contain_more_than_280_characters(self):
        form = PostForm(data = self.form_input)
        self.form_input['text'] = 'x' * 281
        self.assertFalse(form.is_valid())








    # def test_form_uses_model_validation(self):
    #     self.form_input['username'] = 'badusername'
    #     form = SignUpForm(data= self.form_input)
    #     self.assertFalse(form.is_valid())
    #
    #
    # #New password has correct format
    # def test_password_must_contain_uppercase_character(self):
    #     self.form_input['new_password'] = 'password123'
    #     self.form_input['password_confirmation'] = 'password123'
    #     form = SignUpForm(data = self.form_input)
    #     self.assertFalse(form.is_valid())
    #
    # def test_password_must_contain_lowercase_character(self):
    #     self.form_input['new_password'] = 'PASSWORD123'
    #     self.form_input['password_confirmation'] = 'PASSWORD123'
    #     form = SignUpForm(data = self.form_input)
    #     self.assertFalse(form.is_valid())
    #
    # def test_password_must_contain_number(self):
    #     self.form_input['new_password'] = 'PasswordABC'
    #     self.form_input['password_confirmation'] = 'PasswordABC'
    #     form = SignUpForm(data = self.form_input)
    #     self.assertFalse(form.is_valid())
    #
    #
    # def test_new_password_and_password_confirmation_are_identical(self):
    #     self.form_input['password_confirmation'] = 'WrongPassword123'
    #     form = SignUpForm(data = self.form_input)
    #     self.assertFalse(form.is_valid())
    #
    # def test_form_must_save_correctly(self):
    #     form = SignUpForm(data=self.form_input)
    #     before_count = User.objects.count()
    #     form.save()
    #     after_count = User.objects.count()
    #     self.assertEqual(after_count, before_count + 1)
    #     user = User.objects.get(username = '@janedoe')
    #     self.assertEqual(user.first_name, 'Jane')
    #     self.assertEqual(user.last_name, 'Doe')
    #     self.assertEqual(user.email, 'janedoe@example.org')
    #     self.assertEqual(user.bio, 'My bio')
    #     is_password_correct = check_password('Password123', user.password)
    #     self.assertTrue(is_password_correct)
