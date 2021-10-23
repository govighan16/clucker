"""Unit tests of the post model."""
from django.test import TestCase
from microblogs.models import User
from microblogs.models import Post


class PostTestCase(TestCase):
    """Unit tests of the post model."""

    def setUp(self):

     u1 = User.objects.create_user(
     username ='@johndoe',
     first_name = 'john',
     last_name = 'doe',
     email = 'johndoe@example.org',
     password= 'Password123',
     bio = 'Random stuff')
     self.post = Post(author = u1, text = "This is sample text")

    #def test_valid_post(self):
        #self._assert_post_is_valid()















    #def _assert_post_is_valid(self):
        #try:
            #self.post.full_clean()
        #except (ValidationError):
            #self.fail('Test user should fail')

    #def _assert_post_is_invalid(self):
        #with self.assertRaises(ValidationError):
            #self.post.full_clean()
