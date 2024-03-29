# Generated by Django 4.1.1 on 2023-01-31 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiclabsite', '0008_single_song_single'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='single',
        ),
        migrations.AddField(
            model_name='single',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='audio/'),
        ),
        migrations.AddField(
            model_name='single',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='single',
            name='name',
            field=models.CharField(max_length=1000),
        ),
    ]
