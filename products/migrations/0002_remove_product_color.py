# Generated by Django 5.0.1 on 2024-05-21 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
    ]
