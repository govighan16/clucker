"""Unit tests for the user model."""
from django.core.exceptions import ValidationError
from django.test import TestCase
from microblogs.models import User


class UserModelTest(TestCase):
    """Unit tests for the user model."""

    fixtures = [
         'microblogs/tests/fixtures/default_user.json',
         'microblogs/tests/fixtures/other_users.json'
    ]

    def setUp(self):
        self.user = User.objects.get(username='@johndoe')


    def test_valid_user(self):
        self._assert_user_is_valid()


    def test_username_cannot_be_blank(self):
         self.user.username = ''
         self._assert_user_is_invalid()

    def test_username_can_be_30_characters_long(self):
        self.user.username = '@' + 'x' * 29
        self._assert_user_is_valid()

    def test_username_cannot_be_over_30_characters_long(self):
        self.user.username = '@' + 'x' * 30
        self._assert_user_is_invalid()

    def test_username_must_be_unique(self):
        second_user = User.objects.get(username='@janedoe')
        self.user.username = second_user.username
        self._assert_user_is_invalid()

    def test_username_must_start_with_at_symbol(self):
        self.user.username = 'johndoe'
        self._assert_user_is_invalid()

    def test_username_must_contain_only_alphanumbericals_after_at(self):
        self.user.username = '@john!doe'
        self._assert_user_is_invalid()

    def test_username_must_contain_at_least_3_alphanumbericals_after_at(self):
        self.user.username = '@jo'
        self._assert_user_is_invalid()

    def test_username_may_contain_numbers(self):
        self.user.username = '@john123'
        self._assert_user_is_valid()

    def test_username_must_contain_only_one_at(self):
        self.user.username = '@@johndoe'
        self._assert_user_is_invalid()

    def test_firstname_must_not_be_blank(self):
        self.user.first_name = ''
        self._assert_user_is_invalid()

    def test_firstname_may_already_exist(self):
        second_user = User.objects.get(username='@janedoe')
        self.user.first_name = second_user.first_name
        self._assert_user_is_valid()

    def test_firstname_has_a_maximum_of_50_characters(self):
        self.user.first_name = 'x' * 51
        self._assert_user_is_invalid()

    def test_firstname_may_contain_50_characters(self):
        self.user.first_name = 'x' * 50
        self._assert_user_is_valid()

    def test_lastname_must_not_be_blank(self):
        self.user.last_name = ''
        self._assert_user_is_invalid()

    def test_lastname_may_already_exist(self):
        second_user = User.objects.get(username='@janedoe')
        self.user.last_name = second_user.last_name
        self._assert_user_is_valid()

    def test_lastname_has_a_maximum_of_50_characters(self):
        self.user.last_name = 'x' * 51
        self._assert_user_is_invalid()

    def test_lastname_may_contain_50_characters(self):
        self.user.last_name = 'x' * 50
        self._assert_user_is_valid()

    def test_email_must_be_unique(self):
        self.user.email = 'janedoe@example.org'
        second_user = User.objects.get(username='@janedoe')
        self._assert_user_is_invalid()

    def test_email_must_not_be_blank(self):
        self.user.email = ''
        self._assert_user_is_invalid()

    def test_email_is_appropriate(self):
        self.user.email = 'lolol@@kcl..org'
        self._assert_user_is_invalid()

    def test_email_must_contain_username(self):
        self.user.email = '@kcl.org'
        self._assert_user_is_invalid()

    def test_email_must_contain_domain_name(self):
        self.user.email = 'johndoe@.org'
        self._assert_user_is_invalid()

    def test_email_must_contain_domain_(self):
        self.user.email = 'johndoe@example'
        self._assert_user_is_invalid()

    def test_email_must_contain_at_symbol(self):
        self.user.email = 'johndoe.org'
        self._assert_user_is_invalid()

    def test_bio_may_be_blank(self):
        self.user.bio = ''
        self._assert_user_is_valid()

    def test_bio_may_exist(self):
        second_user = User.objects.get(username='@janedoe')
        self.user.bio = second_user.bio
        self._assert_user_is_valid()

    def test_bio_must_not_contain_more_than_520_characters(self):
        self.user.bio = 'x' * 521
        self._assert_user_is_invalid()

    def test_bio_may_contain_520_characters(self):
        self.user.bio = 'x' * 520
        self._assert_user_is_valid()

    def test_toggle_follow_user(self):
        jane = User.objects.get(username='@janedoe')
        self.assertFalse(self.user.is_following(jane))
        self.assertFalse(jane.is_following(self.user))
        self.user.toggle_follow(jane)
        self.assertTrue(self.user.is_following(jane))
        self.assertFalse(jane.is_following(self.user))
        self.user.toggle_follow(jane)
        self.assertFalse(self.user.is_following(jane))
        self.assertFalse(jane.is_following(self.user))

    def test_follow_counters(self):
        jane = User.objects.get(username='@janedoe')
        petra = User.objects.get(username='@petrapickles')
        peter = User.objects.get(username='@peterpickles')
        self.user.toggle_follow(jane)
        self.user.toggle_follow(petra)
        self.user.toggle_follow(peter)
        jane.toggle_follow(petra)
        jane.toggle_follow(peter)
        self.assertEqual(self.user.follower_count(), 0)
        self.assertEqual(self.user.followee_count(), 3)
        self.assertEqual(jane.follower_count(), 1)
        self.assertEqual(jane.followee_count(), 2)
        self.assertEqual(petra.follower_count(), 2)
        self.assertEqual(petra.followee_count(), 0)
        self.assertEqual(peter.follower_count(), 2)
        self.assertEqual(peter.followee_count(), 0)

    def test_user_cannot_follow_self(self):
        self.user.toggle_follow(self.user)
        self.assertEqual(self.user.follower_count(),0)
        self.assertEqual(self.user.followee_count(),0)


    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail('Test user should fail')

    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()
