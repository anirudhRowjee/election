# Generated by Django 2.1.5 on 2019-02-05 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoterLists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=30)),
                ('file', models.FileField(upload_to='media/voterlists/')),
                ('migrated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
