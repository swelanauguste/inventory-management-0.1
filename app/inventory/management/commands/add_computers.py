from random import randint

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Computer, ComputerModel, Supplier


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        f_supplier = Supplier.objects.earliest("pk").pk
        l_supplier = Supplier.objects.latest("pk").pk
        f_model = ComputerModel.objects.earliest("pk").pk
        l_model = ComputerModel.objects.latest("pk").pk

        fake = Faker()
        for _ in range(200):
            computer = Computer.objects.get_or_create(
                serial_number=fake.msisdn(),
                model=ComputerModel.objects.get(pk=randint(f_model, l_model)),
                supplier=Supplier.objects.get(pk=randint(f_supplier, l_supplier)),
            )
        self.stdout.write(self.style.SUCCESS(f"Computer added"))
