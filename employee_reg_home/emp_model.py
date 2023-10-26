from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    doj = models.DateField(null=True, blank=True)  # Date of Joining
    present_address = models.TextField(blank=True)
    permanent_address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    contact_no = models.CharField(max_length=15, blank=True)
    adhar_no = models.CharField(max_length=12, blank=True)  # Aadhar Number
    epf_no = models.CharField(max_length=15, blank=True)
    esi_no = models.CharField(max_length=15, blank=True)
    pan_no = models.CharField(max_length=10, blank=True)
    bank_name = models.CharField(max_length=100, blank=True)
    acc_no = models.CharField(max_length=20, blank=True)
    ifse = models.CharField(max_length=15, blank=True)  # IFSC Code
    branch = models.CharField(max_length=100, blank=True)
    bg = models.CharField(max_length=5, blank=True)  # Blood Group
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    nationality = models.CharField(max_length=50, blank=True)
    religion = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50, blank=True)
    education = models.CharField(max_length=100, blank=True)
    last_pay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)

# Employee Salary class 
class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    monthly_salary = models.IntegerField(null=True,blank=True)
    gross_salary_ctc = models.IntegerField(null=True,blank=True)
    employee_type = models.CharField(max_length=100)
    

    # def save(self, *args, **kwargs):
    #     if self._state.adding and self.monthly_salary is not None and self.balance_amount is None:
    #         self.balance_amount = self.monthly_salary
    #     super(EmployeeSalary, self).save(*args, **kwargs)

class UpdateSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    advance_amount = models.IntegerField(null=True,blank=True)
    balance_amount = models.IntegerField(null=True,blank=True)
    adv_paid_date = models.DateField(null=True, blank=False,unique=True)


    