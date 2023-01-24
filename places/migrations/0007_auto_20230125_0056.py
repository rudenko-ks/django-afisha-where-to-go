# Generated by Django 3.2.16 on 2023-01-24 21:56

from django.db import migrations


def delete_inconsistent_images(apps, scheme_editor):
    Image = apps.get_model('places', 'Image')
    for image in Image.objects.all().iterator():
        if not image.image:
            image.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_image_place'),
    ]

    operations = [migrations.RunPython(delete_inconsistent_images)]
