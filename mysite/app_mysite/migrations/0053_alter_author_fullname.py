# Generated by Django 4.1.7 on 2023-03-27 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mysite', '0052_alter_author_id_alter_quote_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='fullname',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]