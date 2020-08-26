# Generated by Django 3.0.8 on 2020-08-26 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200824_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='Favorite_genre',
            field=models.CharField(choices=[('YA', 'Young Adult'), ('RO', 'Romance'), ('FA', 'Fantasy'), ('SF', 'Sci-Fi'), ('NF', 'Non-Fiction'), ('GN', 'Graphic Novels & Comics'), ('MY', 'Mystery'), ('HF', 'Historical Fiction'), ('HO', 'Horror'), ('TH', 'Thriller'), ('PO', 'Poetry')], default='Sci-Fi', max_length=100),
            preserve_default=False,
        ),
    ]
