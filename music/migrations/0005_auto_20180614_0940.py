# Generated by Django 2.0.6 on 2018-06-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_song_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='logo',
            field=models.FileField(upload_to=''),
        ),
    ]