# Generated by Django 3.1 on 2020-09-06 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
