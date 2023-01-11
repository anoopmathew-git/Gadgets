# Generated by Django 4.1.2 on 2023-01-02 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MYapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='catdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('cdes', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
