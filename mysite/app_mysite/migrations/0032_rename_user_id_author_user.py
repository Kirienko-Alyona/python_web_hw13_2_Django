# Generated by Django 4.1.7 on 2023-03-27 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_mysite', '0031_author_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='user_id',
            new_name='user',
        ),
    ]
