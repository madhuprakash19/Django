import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

from faker import Faker
from AppTwo.models import Users
fake = Faker()

def populate(N=5):
	for entry in range(N):
		fake_first = fake.first_name()
		fake_last = fake.last_name()
		fake_email = fake.email()

		Users.objects.get_or_create(first_name = fake_first , last_name = fake_last , email = fake_email)[0]

if __name__ == '__main__':
	print("Populating script!")
	populate(20)
	print("Populating complete!")
