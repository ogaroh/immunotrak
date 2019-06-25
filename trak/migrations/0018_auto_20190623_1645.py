# Generated by Django 2.2 on 2019-06-23 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trak', '0017_county'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='county',
            name='code',
        ),
        migrations.RemoveField(
            model_name='county',
            name='vaccinations',
        ),
        migrations.AlterField(
            model_name='location',
            name='county',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trak.County'),
        ),
    ]