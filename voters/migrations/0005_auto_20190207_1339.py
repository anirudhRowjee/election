# Generated by Django 2.1.5 on 2019-02-07 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0004_voters_is_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voters',
            name='has_voted',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='voters',
            name='is_candidate',
            field=models.CharField(default='N', max_length=1),
        ),
    ]
