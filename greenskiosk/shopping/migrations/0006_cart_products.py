# Generated by Django 3.1 on 2020-09-06 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_auto_20200906_1250'),
        ('shopping', '0005_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='catalogue.Product'),
        ),
    ]
