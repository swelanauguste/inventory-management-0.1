from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Employee


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(200):
            name = f"{fake.first_name()} {fake.last_name()}"
            ext = fake.msisdn()[:4]
            Employee.objects.get_or_create(name=name, ext=ext)
            self.stdout.write(self.style.SUCCESS(f"{name}"))
