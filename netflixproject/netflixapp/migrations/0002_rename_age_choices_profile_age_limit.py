# Generated by Django 4.2.2 on 2023-08-04 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netflixapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='age_choices',
            new_name='age_limit',
        ),
    ]
