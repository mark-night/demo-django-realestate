# Generated by Django 3.0.8 on 2020-07-07 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
