from django.db import models
from nepali_date import NepaliDate
import datetime
# Create your models here.
class Loantype(models.Model):
    loantype = models.CharField(max_length=100)
    interest = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    #def __str__(self)

class Loan(models.Model):
    STATUS_CHOICES=(
    ('DRAFTS','drafts'),
    ('ARCHIVE','archive'),
    ('VERIFIED','verified'),
    )
    loantype_id = models.OneToOneField(Loantype,on_delete=models.CASCADE,primary_key=True)
    employee_name = models.CharField(max_length=100)
    loanamount = models.IntegerField()
    status=models.CharField(choices=STATUS_CHOICES)
    empoyee_id=models.IntegerField()
    permanent_address=models.CharField(max_length=100)
    temporary_address=models.CharField(max_length=100)
    #DOB=
    #recuitdate=
    #position=
print(NepaliDate.today())
#print(NepaliDate.today(lang='nep'))
