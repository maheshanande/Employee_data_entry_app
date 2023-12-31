"""
URL configuration for nscb_data_entry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee_reg_home import views

app_name = 'nscb'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.Employee_reg_page,name='home'),
    path('signup/',views.admin_register, name='register'),
    path('',views.admin_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('Emp_reg/',views.employee_reg,name='empReg'),
    path('Attendence_marker/',views.Attendance_marker,name='attendenceMark'),
    path('Salary_details/',views.add_salary,name='salaryUpdate'),
    path('Update_employee/',views.update_salary_data,name='employeeUpdate'),
    path('data/',views.get_employee_data,name='data'),
    path('Adv_data/',views.advance_payment_data,name='Advancedata'),
    path('delete_data/',views.delete_emp,name='deleteData'),
    path('payment_reg/',views.payment_data,name='paymentReg'),
    path('Payment_data/',views.payment_data_view,name='paymentData'),
    path('calculate_balance_amount/',views.calculate_balance_amount,name='calcpay'),

]
