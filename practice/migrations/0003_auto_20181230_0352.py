# Generated by Django 2.1 on 2018-12-30 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subdomain',
            name='link',
        ),
        migrations.RemoveField(
            model_name='subdomain',
            name='selection',
        ),
    ]
