# Generated by Django 4.1.5 on 2023-01-29 09:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.TextField(default=django.utils.timezone.now, help_text='Appointment Title', verbose_name='Appointment Title'),
            preserve_default=False,
        ),
    ]
