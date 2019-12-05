from django.db import models
from nepali_date import NepaliDate
import datetime


# Create your models here.
def TODAY_NEPALI_DATE():
    nepal= (NepaliDate.today())
    var=str(nepal)
    var1=var.replace('BS','')
    var2=var1.replace(' ','')
    var3=var2.replace('/','-')
    return var3
class Loantype(models.Model):
    loantype = models.CharField(max_length=100)
    interest = models.CharField(max_length=30)
    period_years = models.FloatField()
    num_payments_per_year = models.FloatField()
    start_date = models.DateField()
    created_on = models.CharField(max_length=100,default=TODAY_NEPALI_DATE())
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} at {} for {} years".format(self.loantype, self.interest, self.period_years)


class Loan(models.Model):
    STATUS_CHOICES=(
    ('DRAFTS','drafts'),
    ('ARCHIVE','archive'),
    ('VERIFIED','verified'),
    )

    loantype_id = models.OneToOneField(Loantype,on_delete=models.CASCADE,primary_key=True)
    employee_name = models.CharField(max_length=100)
    loanamount = models.IntegerField()
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='DRAFTS')
    employee_id=models.IntegerField()
    permanent_address=models.CharField(max_length=100)
    temporary_address=models.CharField(max_length=100)
    DOB=models.DateField()
    recruitdate=models.DateField()
    position=models.CharField(max_length=100)
    submission_form = models.ImageField(null=True)
    lalpurja = models.ImageField(null=True)
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

    def __str__(self):
        return "{} - {}".format(self.employee_name, self.status)

#print(NepaliDate.today())
#print(NepaliDate.today(lang='nep'))
class Payment(models.Model):
    payment_amount = models.IntegerField()
    loan_id = models.OneToOneField(Loan,on_delete=models.CASCADE,primary_key=True)
    payment_date = models.DateField()
    updated_on = models.DateTimeField(auto_now=True)

    # def __str__(self):
        # return "{}"
