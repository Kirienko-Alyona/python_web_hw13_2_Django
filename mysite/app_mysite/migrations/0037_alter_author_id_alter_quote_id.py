# Generated by Django 4.1.7 on 2023-03-27 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mysite', '0036_author_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='quote',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
