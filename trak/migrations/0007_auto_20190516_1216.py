# Generated by Django 2.2 on 2019-05-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trak', '0006_auto_20190516_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('parent_id', models.DecimalField(decimal_places=0, max_digits=50)),
            ],
        ),
        migrations.RenameField(
            model_name='child',
            old_name='parent_id',
            new_name='child_id',
        ),
    ]