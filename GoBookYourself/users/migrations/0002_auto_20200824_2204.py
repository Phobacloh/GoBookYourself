# Generated by Django 3.0.8 on 2020-08-24 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(default='Who am I?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_pic',
            field=models.URLField(default='https://cdn.mos.cms.futurecdn.net/hKm2MuLdDLubD6rgeYLeDM-650-80.jpg.webp'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='tagline',
            field=models.CharField(default='Books are a uniquely portable magic', max_length=200),
            preserve_default=False,
        ),
    ]
