import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        Phone.objects.bulk_create([
            Phone(
                name=line['name'],
                image=line['image'], 
                price=line['price'],
                release_date=line['release_date'],
                lte_exists=line['lte_exists'],
                slug=slugify(line['name'])
            )
            for line in phones
        ])
