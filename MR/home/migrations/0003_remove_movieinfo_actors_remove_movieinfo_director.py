# Generated by Django 4.1 on 2024-07-02 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_rate_movieinfo_runtime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieinfo',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='movieinfo',
            name='director',
        ),
    ]
