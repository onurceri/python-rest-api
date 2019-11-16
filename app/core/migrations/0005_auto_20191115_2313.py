# Generated by Django 2.2.7 on 2019-11-15 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191115_2249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterField(
            model_name='customermailaddress',
            name='customer_id',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='mail_addresses',
                to='core.Customer'
            ),
        ),
    ]