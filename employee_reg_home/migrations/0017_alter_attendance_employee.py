# Generated by Django 4.2.6 on 2023-10-26 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_reg_home', '0016_alter_attendance_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_reg_home.employee'),
        ),
    ]
