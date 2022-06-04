# Generated by Django 4.0.5 on 2022-06-04 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immfly_api', '0004_alter_channel_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='picture_path',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='content_path',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='metadata',
            field=models.JSONField(null=True),
        ),
    ]