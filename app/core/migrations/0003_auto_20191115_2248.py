# Generated by Django 2.2.7 on 2019-11-15 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_customermailaddress_customertype_customertypemap'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customermailaddress',
            name='is_deleted',
        ),
        migrations.AddField(
            model_name='customermailaddress',
            name='is_deleteWd',
            field=models.BooleanField(default=False),
        ),
    ]
