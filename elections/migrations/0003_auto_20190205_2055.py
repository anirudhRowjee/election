# Generated by Django 2.1.5 on 2019-02-05 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0002_voterlists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voterlists',
            name='filename',
            field=models.CharField(max_length=100),
        ),
    ]
