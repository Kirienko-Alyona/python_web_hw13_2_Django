# Generated by Django 4.1.7 on 2023-03-26 23:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mysite', '0022_alter_quote_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, size=None),
        ),
    ]
