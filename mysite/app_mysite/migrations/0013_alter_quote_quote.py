# Generated by Django 4.1.7 on 2023-03-26 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mysite', '0012_alter_quote_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote',
            field=models.TextField(null=True, unique=True),
        ),
    ]
