from django.db import models

# Create your models here.
class Patient(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()

class ClinicalData(models.Model):
    COMPONENT_NAME = [('hw','Height/Weight'),('bp','Blood Pressure'),('heart rate','Heart Rate')]
    componentname = models.CharField(choices = COMPONENT_NAME,max_length=50)
    componentvalue = models.CharField(max_length=50)
    measureddatetime = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient,on_delete = models.CASCADE)