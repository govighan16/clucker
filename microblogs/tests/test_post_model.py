"""Unit tests of the post model."""
from django.test import TestCase
from microblogs.models import User
from microblogs.models import Post
from django.core.exceptions import ValidationError

class PostTestCase(TestCase):
    """Unit tests of the post model."""

    def setUp(self):
       super(TestCase, self).setUp()
       u1 = User.objects.create_user(
       username ='@johndoe',
       first_name = 'john',
       last_name = 'doe',
       email = 'johndoe@example.org',
       password= 'Password123',
       bio = 'Random stuff')
       self.user = u1
       self.post = Post(author = u1, text = "This is sample text")

    def test_valid_message(self):
        try:
            self.post.full_clean()
        except ValidationError:
            self.fail("Test message should be valid")

    def test_text_must_not_be_blank(self):
        self.post.text = ''
        with self.assertRaises(ValidationError):
            self.post.full_clean()

    #def test_valid_post(self):
        #self._assert_post_is_valid()

    def test_author_cannot_be_blank(self):
        self.post.author = None
        with self.assertRaises(ValidationError):
            self.post.full_clean()
        #self._assert_post_is_invalid()

      #def test_post_is_deleted_when_author_is_deleted(self):
        #self.user.delete()
        #if self.post.author == None :
        #    self._assert_post_is_valid()

    #def test_post_only_contains_up_to_280_characters_long(self):
        #self.post.text = 'x' * 280
        #self._assert_post_is_valid()

    def test_post_must_not_contain_more_than_280_characters_long(self):
        self.post.text = 'x' * 281
        with self.assertRaises(ValidationError):
            self.post.full_clean()
        #self._assert_post_is_invalid()

      #def test_check_if_post_is_ordered_in_decreasing_order_of_recency(self):
        #p2 = Post(author = self.user, text = "This is the second post")
        #p3 = Post(author = self.user, text = "This is the third post")

        #if self.post.created_at < p2.created_at < p3.created_at:
        #    self._assert_post_is_valid()






















    def _assert_post_is_valid(self):
        try:
            self.post.full_clean()
        except (ValidationError):
           self.fail('Test post should fail')

    def _assert_post_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.post.full_clean()
