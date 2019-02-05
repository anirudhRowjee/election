# Generated by Django 2.1.5 on 2019-02-05 06:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2019)),
                ('election_number', models.IntegerField(default=1)),
                ('is_active', models.BooleanField(default=False)),
                ('type', models.CharField(default='General Election', max_length=50)),
                ('created_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='election',
            unique_together={('year', 'election_number')},
        ),
    ]
