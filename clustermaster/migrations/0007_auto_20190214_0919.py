# Generated by Django 2.1.5 on 2019-02-14 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clustermaster', '0006_auto_20190214_0913'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cluster',
            unique_together=set(),
        ),
    ]