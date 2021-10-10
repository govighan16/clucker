from django.core.management.base import BaseCommand, CommandError
from faker import Faker

class Command(BaseCommand):

    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')


    def generateText(self):
        self.faker.text()



    def handle(self, *args, **options):
        print("WARNING: The seed command has not yet been implemented yet.")
        self.generateText()
