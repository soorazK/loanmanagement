from django.contrib.auth.models import AbstractUser
from django.db import models
from nepali_date import NepaliDate
import datetime


# Create your models here.
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return '{}'.format(self.username)

    
def TODAY_NEPALI_DATE():
    nepal= (NepaliDate.today())
    var=str(nepal)
    var1=var.replace('BS','')
    var2=var1.replace(' ','')
    var3=var2.replace('/','-')
    return var3



class Loantype(models.Model):
    loantype = models.CharField(max_length=100)
    interest = models.FloatField(default=0)
    period_years = models.FloatField(default=0.0)
    num_payments_per_year = models.FloatField(default=0.0)
    start_date = models.DateField(default=0.0)
    created_on = models.CharField(max_length=100,default=TODAY_NEPALI_DATE())
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.loantype
def folder(instance,filename):
    return '{}/{}'.format(instance.employee_name,filename)

class Loan(models.Model):
    STATUS_CHOICES=(
    ('DRAFTS','drafts'),
    ('STAGE ONE PENDING', 'stage_one_pending'),
    ('STAGE ONE VERIFIED', 'stage_one_verified'),
    ('STAGE TWO PENDING', 'stage_two_pending'),
    ('STAGE TWO VERIFIED', 'stage_two_verified'),
    ('ARCHIVED','archived'),
    )
    loanname = models.ForeignKey(Loantype,on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    loanamount = models.IntegerField()
    status=models.CharField(max_length=25,choices=STATUS_CHOICES,default='DRAFTS')
    employee_id=models.IntegerField()
    permanent_address=models.CharField(max_length=100)
    temporary_address=models.CharField(max_length=100)
    DOB=models.DateField()
    recruitdate=models.DateField()
    position=models.CharField(max_length=100)
    submission_form = models.ImageField(null=True)
    lalpurja = models.ImageField(upload_to=folder,null=True)
    malpot_receipt_1 = models.ImageField(null=True)
    malpot_receipt_2 = models.ImageField(null=True)
    verified_map = models.ImageField(null=True)
    blue_print = models.ImageField(null=True)
    committee_sifaris = models.ImageField(null=True)
    marriage_certificate = models.ImageField(null=True)
    mun_vdc_sifaris = models.ImageField(null=True)
    dristibandha = models.ImageField(null=True)
    close_house_photo = models.ImageField(null=True)
    inspection_report = models.ImageField(null=True)
    anusuchi_six_form = models.ImageField(null=True)
    tippani = models.ImageField(null=True)
    voucher = models.ImageField(null=True)
    debit_credit = models.ImageField(null=True)
    quotation = models.ImageField(null=True)
    memo = models.ImageField(null=True)
    credit_note = models.ImageField(null=True)
    approved_letter = models.ImageField(null=True)


    #def __str__(self):
    #    return "{} - {}".format(self.employee_name, self.status)

#print(NepaliDate.today())
#print(NepaliDate.today(lang='nep'))
class Payment(models.Model):
    payment_amount = models.IntegerField()
    loan = models.ForeignKey(Loan,on_delete=models.CASCADE)
    payment_date = models.DateField()
    updated_on = models.DateTimeField(auto_now=True)

    # def __str__(self):
        # return "{}"
#class Setup(models.Model):
#    logo=models.ImageField(null=True)
