# Generated by Django 3.2 on 2021-05-04 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audit',
            old_name='Author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='audit',
            old_name='Readers',
            new_name='readers',
        ),
    ]
