# Generated by Django 2.1 on 2020-01-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userrequests',
            fields=[
                #('_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                #('id', models.IntegerField(primary_key=True)),
                ('OHRID', models.IntegerField()),
                ('url', models.CharField(max_length=200)),
                ('subnet', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('frequency', models.IntegerField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
