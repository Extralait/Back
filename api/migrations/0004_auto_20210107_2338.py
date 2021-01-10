# Generated by Django 3.1.4 on 2021-01-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_organization_video_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='internship',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='practice',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='work',
        ),
        migrations.AddField(
            model_name='organization',
            name='detail',
            field=models.TextField(blank=True, null=True, verbose_name='Код направления'),
        ),
        migrations.DeleteModel(
            name='Internship',
        ),
        migrations.DeleteModel(
            name='Practice',
        ),
        migrations.DeleteModel(
            name='Work',
        ),
    ]