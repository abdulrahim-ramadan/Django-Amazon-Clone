# Generated by Django 5.0.1 on 2024-03-15 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_delveryfee'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DelveryFee',
            new_name='DeliveryFee',
        ),
    ]