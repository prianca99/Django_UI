# Generated by Django 2.1 on 2020-03-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_userrequests_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequests',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
