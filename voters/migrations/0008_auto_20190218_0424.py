# Generated by Django 2.1.5 on 2019-02-18 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0007_auto_20190214_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voters',
            name='voter_class',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
