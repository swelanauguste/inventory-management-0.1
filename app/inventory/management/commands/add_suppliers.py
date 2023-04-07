from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Supplier


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(200):
            Supplier.objects.get_or_create(
                name=fake.company(),
                address=fake.street_address(),
                address1=fake.city(),
                phone=fake.msisdn(),
                email=fake.profile()["mail"],
            )
            self.stdout.write(self.style.SUCCESS(f"{name}"))
