# Generated by Django 3.1.6 on 2021-02-21 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='copy_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
