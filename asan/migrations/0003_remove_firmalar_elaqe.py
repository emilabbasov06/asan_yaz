# Generated by Django 4.2.16 on 2024-12-31 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asan', '0002_remove_firmalar_unvan_firmalar_magaza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firmalar',
            name='elaqe',
        ),
    ]