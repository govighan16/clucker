from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from faker import Faker
from django.contrib.auth import get_user_model #

User = get_user_model()


class Command(BaseCommand):

    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')


# self.user = User.objects.create_user(
#     '@johndoe',
#     first_name = 'John',
#     last_name = 'Doe',
#     email = 'johndoe@example.org',
#     password = 'Password123',
#     bio = 'The quick brown fox jumps over the lazy dog'
# )



    def handle(self, *args, **options):
        #print("WARNING: The seed command has not yet been implemented yet.")
        #print('@' + self.faker.user_name())
        for i in range(100):
        #user = User.objects.create_user(self.fake.first_name(), self.fake.last_name(), self.fake.email(),self.faker.password(), self.fake.text())
            user = User.objects.create_user(username = '@' + self.faker.user_name(), first_name = self.faker.first_name(), last_name = self.faker.last_name(), email = self.faker.email(), password = self.faker.password(), bio = self.faker.text())
            user.save()


            #print(user.bio)
