from django.db import models
from nepali_date import NepaliDate
import datetime


# Create your models here.
class Loantype(models.Model):
    type = models.CharField(max_length=100)
    interest = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    #def __str__(self)

class Loan(models.Model):
    loantype_id = models.OneToOneField(Loantype,on_delete=models.CASCADE,primary_key=True)
    employee_name = models.CharField(max_length=100)
    loanamount = models.IntegerField()
    status=models.BooleanField()

#print(NepaliDate.today())
#print(NepaliDate.today(lang='nep'))
