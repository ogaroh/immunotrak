# Generated by Django 2.2 on 2019-06-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trak', '0019_county_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]