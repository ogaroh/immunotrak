# Generated by Django 2.2 on 2019-06-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trak', '0018_auto_20190623_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='county',
            name='code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
