# Generated by Django 3.2 on 2021-05-02 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='interest',
            field=models.FloatField(),
        ),
    ]
