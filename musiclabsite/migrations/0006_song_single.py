# Generated by Django 4.1.1 on 2023-01-27 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musiclabsite', '0005_single'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='single',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musiclabsite.single'),
        ),
    ]