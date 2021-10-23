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
        #for i in range(100:
        #user = User.objects.create_user(self.fake.first_name(), self.fake.last_name(), self.fake.email(),self.faker.password(), self.fake.text())
            #listUsers = User.objects.all()
            #print(listUsers)
            #u = User.objects.all()
            #print(User.objects.count())
            #for i in range(2, User.objects.count()-1):

            #print(User.objects.all()[2:User.objects.count()])
            u = User.objects.all()[2:User.objects.count()]
            for i in range(len(u)):
                user = u[i]
                user.delete()
