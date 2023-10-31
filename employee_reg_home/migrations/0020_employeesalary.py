# Generated by Django 4.2.6 on 2023-10-30 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_reg_home', '0019_delete_employeesalary'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthly_salary', models.IntegerField(blank=True, null=True)),
                ('gross_salary_ctc', models.IntegerField(blank=True, null=True)),
                ('employee_type', models.CharField(max_length=100)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_reg_home.employee')),
            ],
        ),
    ]
