# Generated by Django 3.1.4 on 2021-01-15 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210116_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=40, unique=True, verbose_name='email'),
        ),
    ]