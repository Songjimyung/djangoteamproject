# Generated by Django 4.2 on 2023-04-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]