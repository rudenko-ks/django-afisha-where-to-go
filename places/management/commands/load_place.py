from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from places.models import Place, Image

import requests


class Command(BaseCommand):
    help = 'Upload place from JSON URL to website.'

    def add_arguments(self, parser):
        parser.add_argument('load_place', type=str, help='URL to JSON file with place description.')

    def handle(self, *args, **options):
        place_info_url = options['load_place']
        response = requests.get(place_info_url)
        response.raise_for_status()
        place_info = response.json()
        coordinates = place_info['coordinates']

        place, created = Place.objects.get_or_create(
            title=place_info['title'],
            longitude=coordinates['lng'],
            latitude=coordinates['lat'],
            defaults={
                'description_short': place_info.get('description_short', ''),
                'description_long': place_info.get('description_long', '')
            },
        )
        if created:
            for num, img_url in enumerate(place_info.get('imgs', [])):
                response = requests.get(img_url)
                response.raise_for_status()
                img_name = img_url.split('/')[-1]
                img_file = ContentFile(content=response.content, name=img_name)
                Image.objects.get_or_create(place=place, number=num, image=img_file)
