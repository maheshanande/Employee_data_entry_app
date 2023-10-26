# Generated by Django 4.2.6 on 2023-10-25 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_reg_home', '0005_employeesalary'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeesalary',
            name='adv_paid_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employeesalary',
            name='advance_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employeesalary',
            name='balance_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employeesalary',
            name='gross_salary_ctc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employeesalary',
            name='monthly_salary',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
