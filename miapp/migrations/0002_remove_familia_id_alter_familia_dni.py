# Generated by Django 4.0.3 on 2022-03-19 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familia',
            name='id',
        ),
        migrations.AlterField(
            model_name='familia',
            name='DNI',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
