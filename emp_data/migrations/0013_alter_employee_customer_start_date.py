# Generated by Django 4.2 on 2023-05-18 05:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_data', '0012_alter_employee_customer_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='customer_start_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 18, 11, 23, 41, 292728), null=True),
        ),
    ]
