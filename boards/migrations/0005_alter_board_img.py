# Generated by Django 4.2 on 2023-04-13 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_alter_board_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/'),
        ),
    ]