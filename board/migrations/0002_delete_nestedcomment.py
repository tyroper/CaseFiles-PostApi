# Generated by Django 4.0.6 on 2022-07-17 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NestedComment',
        ),
    ]
