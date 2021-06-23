from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=50)
    emp_email = models.EmailField(max_length=50)
    emp_phonenumber = models.CharField(max_length=12)

    def __str__(self):
        return self.emp_name

class EmployeeDesignation(models.Model):
    des_id = models.AutoField(primary_key=True)
    emp_name = models.ForeignKey(EmployeeModel,on_delete=models.CASCADE,related_name='designation')
    emp_designation = models.CharField(max_length=50)
    emp_salary = models.CharField(max_length=12)

    def __str__(self):
        return self.emp_designation

class EmployeeAddress(models.Model):
    emp_name = models.ForeignKey(EmployeeModel,on_delete=models.CASCADE,related_name='address')
    emp_street_name = models.CharField(max_length=100)
    emp_city_name = models.CharField(max_length=100)
    emp_state_name = models.CharField(max_length=75)
    emp_Zip_number = models.CharField(max_length=10)
    emp_country_name = models.CharField(max_length=50)

    def __str__(self):
        return  self.emp_state_name

class EmployeeProfession(models.Model):
    emp_designation = models.ForeignKey(EmployeeDesignation,on_delete=models.CASCADE,related_name='profession')
    emp_profession = models.CharField(max_length=50)

    def __str__(self):
        return self.emp_profession

class EmployeePersonalDetails(models.Model):
    emp_name = models.ForeignKey(EmployeeModel,on_delete=models.CASCADE,related_name="personal_details")
    emp_father_name = models.CharField(max_length=50)
    emp_mother_name = models.CharField(max_length=50)
    emp_father_occupation = models.CharField(max_length=50)
    emp_mother_occupation = models.CharField(max_length=50)
    emp_father_mobile_number = models.CharField(max_length=12)
    
    def __str__(self):
        return self.emp_father_name

