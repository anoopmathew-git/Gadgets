# Generated by Django 4.1.2 on 2023-01-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MYapp', '0003_productdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdb',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
