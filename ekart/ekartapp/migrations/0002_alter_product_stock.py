# Generated by Django 4.0.3 on 2022-05-10 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekartapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
