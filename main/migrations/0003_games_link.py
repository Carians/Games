# Generated by Django 4.1.2 on 2022-10-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_games_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='link',
            field=models.URLField(default=''),
        ),
    ]
