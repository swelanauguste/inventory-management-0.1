from django.core.management.base import BaseCommand

from ...models import Skill

# Skill.objects.all().delete()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(f"static/docs/items.txt") as file:
            for row in file:
                name = row.replace("\n", "")
                Skill.objects.get_or_create(
                    name=name,
                )
                self.stdout.write(self.style.SUCCESS(f"{name} added"))