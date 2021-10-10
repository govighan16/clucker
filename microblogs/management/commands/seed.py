from django.core.management.base import BaseCommand, CommandError
from faker import Faker

class Command(BaseCommand):

    def __init__(self):
        super().__init__()
        self.Faker = Faker('en_GB')


    def handle(self, *args, **options):
        print("WARNING: The seed command has not yet been implemented yet.")
