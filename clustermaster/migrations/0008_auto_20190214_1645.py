# Generated by Django 2.1.5 on 2019-02-14 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clustermaster', '0007_auto_20190214_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booth',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
