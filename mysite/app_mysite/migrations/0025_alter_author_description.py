# Generated by Django 4.1.7 on 2023-03-27 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mysite', '0024_author_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(unique=True),
        ),
    ]
