# Generated by Django 2.2 on 2019-05-22 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trak', '0010_auto_20190522_0859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parent',
            old_name='child',
            new_name='children',
        ),
    ]
