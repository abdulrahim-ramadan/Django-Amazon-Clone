# Generated by Django 5.0.1 on 2024-05-19 15:49

import utils.generate_code
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_address_type_phones_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='code',
            field=models.CharField(default=utils.generate_code.generate_code, max_length=20),
        ),
    ]
