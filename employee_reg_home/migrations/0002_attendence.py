# Generated by Django 4.2.6 on 2023-10-24 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_reg_home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('present', models.CharField(max_length=3)),
                ('overtime', models.CharField(max_length=5)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_reg_home.employee')),
            ],
        ),
    ]
