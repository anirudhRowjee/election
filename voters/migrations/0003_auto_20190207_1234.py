# Generated by Django 2.1.5 on 2019-02-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0002_auto_20190205_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voters',
            name='has_voted',
            field=models.BooleanField(default=False),
        ),
    ]