# Generated by Django 4.1.2 on 2022-10-24 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_games_imgurl_alter_games_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='imgURL',
            field=models.URLField(),
        ),
    ]