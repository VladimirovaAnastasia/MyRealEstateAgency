# Generated by Django 2.2.4 on 2020-02-27 07:03

from django.db import migrations
import phonenumbers


def fill_owners(apps, schema_editor):
    flats = apps.get_model('property', 'Flat')
    owners = apps.get_model('property', 'Owner')

    for flat in flats.objects.all():
        owners.objects.get_or_create(owner_name=flat.owner,
                                     owner_phone_pure=flat.owner_phone_pure,
                                     owners_phonenumber=flat.owners_phonenumber)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(fill_owners),
    ]
