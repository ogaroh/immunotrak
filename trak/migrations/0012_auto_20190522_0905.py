# Generated by Django 2.2 on 2019-05-22 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trak', '0011_auto_20190522_0903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='children',
        ),
        migrations.AddField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='trak.Parent'),
            preserve_default=False,
        ),
    ]
