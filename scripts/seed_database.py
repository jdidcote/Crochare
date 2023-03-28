"""
This script will seed the database with fake data for testing purposes.
The seed_test_data function must be run from the django shell.

Example:
    python manage.py shell
    >>> from scripts.seed_database import seed_test_data
    >>> seed_test_data(n_users=10, n_patterns=10)

"""

from pathlib import Path
import random

from django.contrib.auth.models import User
from patterns.models import CrochetPattern

from faker import Faker

faker = Faker()


class FakeUserInfo:
    def __init__(self):
        first_name = faker.first_name()
        last_name = faker.last_name()
        self.username = f"{first_name.lower()}_{last_name.lower()}"
        self.password = "password"
        self.email = f"{first_name}.{last_name}@example.com"

    def __repr__(self):
        return f"User(username={self.username}, password={self.password}, email={self.email})"


class FakeCrochetPatternInfo:
    def __init__(self):
        self.title = faker.sentence()
        self.description = faker.paragraph()
        self.skill_level = faker.random_element(
            elements=("Easy", "Beginner", "Intermediate", "Advanced")
        )
        self.region = faker.random_element(elements=("UK", "US"))
        self.yarn_weight = faker.random_element(elements=("DK", "4ply"))
        self.hook_size = faker.random_element(elements=("3.5mm", "4mm"))
        self.gauge = faker.random_element(elements=("20sts x 30 rows", "10sts x 10 rows"))
        self.pattern = faker.paragraph()
        self.image = faker.image_url(width=300, height=300)

    def __repr__(self):
        return f"CrochetPattern(title={self.title}, description={self.description}, skill_level={self.skill_level}, " \
               f"region={self.region}, yarn_weight={self.yarn_weight}, hook_size={self.hook_size}, " \
               f"gauge={self.gauge}, pattern={self.pattern}, image={self.image})"


def seed_test_data(n_users=10, n_patterns=10) -> None:
    for _ in range(n_users):
        user_info = FakeUserInfo()
        user = User.objects.create_user(
            username=user_info.username,
            password=user_info.password,
            email=user_info.email
        )
        for _ in range(n_patterns):
            pattern_info = FakeCrochetPatternInfo()
            pattern = CrochetPattern.objects.create(
                title=pattern_info.title,
                description=pattern_info.description,
                skill_level=pattern_info.skill_level,
                region=pattern_info.region,
                yarn_weight=pattern_info.yarn_weight,
                hook_size=pattern_info.hook_size,
                gauge=pattern_info.gauge,
                pattern=pattern_info.pattern,
                image=pattern_info.image,
                author=user
            )