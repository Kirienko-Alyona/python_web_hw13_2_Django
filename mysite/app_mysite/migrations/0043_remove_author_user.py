# Generated by Django 4.1.7 on 2023-03-27 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_mysite', '0042_rename_author_quote_author_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='user',
        ),
    ]
