# Generated by Django 2.1.5 on 2019-02-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0003_auto_20190207_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='voters',
            name='is_candidate',
            field=models.BooleanField(default=False),
        ),
    ]