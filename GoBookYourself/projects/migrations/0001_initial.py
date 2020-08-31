# Generated by Django 3.0.8 on 2020-08-31 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('comment', models.CharField(max_length=200)),
                ('anonymous', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('goal', models.IntegerField()),
                ('image', models.URLField()),
                ('is_open', models.BooleanField()),
                ('date_created', models.DateTimeField()),
                ('date_closed', models.DateTimeField()),
                ('sample', models.TextField()),
                ('category', models.CharField(choices=[('Anything', 'NA'), ('Young Adult', 'YA'), ('Romance', 'RO'), ('Fantasy', 'FA'), ('Sci-Fi', 'SF'), ('Non-Fiction', 'NF'), ('Graphic Novels & Comics', 'GN'), ('Mystery', 'MY'), ('Historical Fiction', 'HF'), ('Horror', 'HO'), ('Thriller', 'TH'), ('Poetry', 'PO')], max_length=100)),
            ],
        ),
    ]
