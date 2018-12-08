# Generated by Django 2.0.5 on 2018-12-08 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0035_auto_20181208_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gogid',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gamelibrary',
            name='games',
            field=models.ManyToManyField(related_name='libraries', to='games.Game'),
        ),
    ]
