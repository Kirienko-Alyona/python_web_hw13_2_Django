# Generated by Django 4.1.7 on 2023-03-28 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_mysite', '0057_alter_author_id_alter_quote_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_mysite.author'),
        ),
    ]
