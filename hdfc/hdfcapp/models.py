from django.db import models

# Create your models here.
class Employee_Details(models.Model):
    EMP_ID=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Designation=models.CharField(max_length=20)
    Qualification=models.CharField(max_length=20)
    class Meta:
        db_table='Employee'




