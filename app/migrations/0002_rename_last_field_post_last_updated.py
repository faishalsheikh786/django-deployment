# Generated by Django 5.1.2 on 2024-10-17 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='last_field',
            new_name='last_updated',
        ),
    ]
