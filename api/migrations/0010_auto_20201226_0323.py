# Generated by Django 3.1.4 on 2020-12-25 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20201222_2145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='min_score',
            new_name='jsons',
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время'),
        ),
    ]
