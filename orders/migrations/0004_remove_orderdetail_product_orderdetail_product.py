# Generated by Django 5.0.1 on 2024-05-09 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_cartdetail_product_and_more'),
        ('products', '0002_alter_review_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='Product',
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_product', to='products.product'),
        ),
    ]
