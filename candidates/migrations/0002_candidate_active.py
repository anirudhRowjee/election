# Generated by Django 2.1.5 on 2019-02-06 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='active',
            field=models.CharField(default='N', max_length=1),
        ),
    ]
