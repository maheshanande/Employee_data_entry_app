# Generated by Django 4.2.6 on 2023-10-31 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_reg_home', '0024_employeesalary_charge_per_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeesalary',
            name='balance_to_pay',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
