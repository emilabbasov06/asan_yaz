# Generated by Django 4.2.16 on 2025-01-01 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asan', '0006_alter_kategoriya_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mehsullar',
            name='kategoriya',
        ),
        migrations.AddField(
            model_name='kategoriya',
            name='mehsul',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='asan.mehsullar'),
        ),
    ]
