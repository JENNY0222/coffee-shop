# Generated by Django 4.0 on 2021-12-20 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffees', '0002_auto_20211206_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffee',
            old_name='grandings',
            new_name='grindings',
        ),
    ]
