# Generated by Django 4.2.6 on 2023-10-31 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_reg_home', '0023_paymentdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeesalary',
            name='charge_per_day',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
