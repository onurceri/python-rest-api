# Generated by Django 2.2.7 on 2019-11-15 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191115_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customertypemap',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customertypemap',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='customertypemap',
            name='type_name',
        ),
        migrations.AddField(
            model_name='customertypemap',
            name='customer',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='customer', to='core.Customer'
            ),
        ),
        migrations.AddField(
            model_name='customertypemap',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type', to='core.CustomerType'),
        ),
    ]
