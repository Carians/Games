# Generated by Django 4.1.2 on 2022-10-24 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_games_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='imgURL',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='games',
            name='link',
            field=models.URLField(),
        ),
    ]
