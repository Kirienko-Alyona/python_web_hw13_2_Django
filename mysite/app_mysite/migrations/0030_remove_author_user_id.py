# Generated by Django 4.1.7 on 2023-03-27 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_mysite', '0029_author_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='user_id',
        ),
    ]
