# Generated by Django 4.2.6 on 2023-10-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_reg_home', '0006_employeesalary_adv_paid_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeesalary',
            name='adv_paid_date',
            field=models.DateField(null=True, unique=True),
        ),
    ]