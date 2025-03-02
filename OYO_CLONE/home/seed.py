import os
import sys
import django

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# Set up Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OYO_CLONE.settings")

# Initialize Django
django.setup()

from django.contrib.auth.models import User
from accounts.models import Hotelvendor, Hotel, Ameneties
from faker import Faker
import random
from random import choice

fake = Faker()

def create_users():
    for _ in range(100):
        email = fake.email()
        Hotelvendor.objects.create(
            email=email,
            business_name=fake.name(),
            username=email,
            first_name=fake.name(),
            phone_number=random.randint(1111111111, 9999999999)
        )

def create_hotels():
    for _ in range(100):
        hotel_vendors = Hotelvendor.objects.all()
        if not hotel_vendors:
            print("No Hotelvendors found. Run create_users() first.")
            return

        hotel_vendor = choice(hotel_vendors)
        amenities = list(Ameneties.objects.all())

        hotel = Hotel.objects.create(
            hotel_name=fake.company(),
            hotel_description=fake.text(),
            hotel_slug=fake.slug(),
            hotel_owner=hotel_vendor,
            hotel_price=fake.random_number(digits=4) / 100.0,
            hotel_offer_price=fake.random_number(digits=4) / 100.0,
            hotel_location=fake.address(),
            is_active=fake.boolean()
        )

        # Add random amenities
        hotel.ameneties.set(random.sample(amenities, min(len(amenities), 5)))

if __name__ == "__main__":
    print("Creating users...")
    create_users()
    print("Users created successfully!")

    print("Creating hotels...")
    create_hotels()
    print("Hotels created successfully!")
