# Generated by Django 4.2.1 on 2023-05-17 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_data', '0006_alter_employee_customer_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='customer_start_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 17, 17, 35, 45, 27634), null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='estatus',
            field=models.CharField(choices=[('Deployed', 'Free'), ('Free', 'Deployed')], max_length=100, null=True),
        ),
    ]
