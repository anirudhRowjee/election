# Generated by Django 2.1.5 on 2019-02-17 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0004_auto_20190212_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='votes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
