# Generated by Django 3.0.8 on 2020-08-26 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_favorite_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='Favorite_genre',
            new_name='favorite_genre',
        ),
    ]