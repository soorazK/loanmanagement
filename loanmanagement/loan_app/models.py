from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from django.db import models
from nepali_date import NepaliDate
import datetime
from django.db.models.signals import pre_save, post_save

from .helpers import random_string_generator, unique_key_generator



# Create your models here.
class CustomUser(AbstractUser):
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=50)

    REQUIRED_FIELDS = ['is_staff', 'email']

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

    recruit_position = models.CharField(max_length=50, null=True, blank=True)
    recruit_level = models.CharField(max_length=50, null=True, blank=True)
    recruit_office = models.CharField(max_length=50, null=True, blank=True)
    current_position = models.CharField(max_length=50, null=True, blank=True)
    current_level = models.CharField(max_length=50, null=True, blank=True)
    current_office = models.CharField(max_length=50, null=True, blank=True)
    citizenship_number = models.CharField(max_length=30, null=True, blank=True)
    citizenship_issued_place = models.CharField(max_length=30, null=True, blank=True)
    citizenship_issued_date = models.CharField(max_length=30, null=True, blank=True)
    loan_for = models.CharField(max_length=50, null=True, blank=True)
    loan_utilization_place = models.CharField(max_length=50, blank=True)
    service_break = models.CharField(max_length=100, null=True, blank=True)
    vacations = models.CharField(max_length=100, null=True, blank=True)
    mobile_number = models.CharField(max_length=10, null=True, blank=True)

    position=models.CharField(max_length=100, blank=True)
    submission_form = models.ImageField(null=True, blank=True)
    lalpurja = models.ImageField(upload_to=folder,null=True, blank=True)
    malpot_receipt_1 = models.ImageField(null=True, blank=True)
    malpot_receipt_2 = models.ImageField(null=True, blank=True)
    verified_map = models.ImageField(null=True, blank=True)
    blue_print = models.ImageField(null=True, blank=True)
    committee_sifaris = models.ImageField(null=True, blank=True)
    marriage_certificate = models.ImageField(null=True, blank=True)
    mun_vdc_sifaris = models.ImageField(null=True, blank=True)
    dristibandha = models.ImageField(null=True, blank=True)
    close_house_photo = models.ImageField(null=True, blank=True)
    inspection_report = models.ImageField(null=True, blank=True)
    anusuchi_six_form = models.ImageField(null=True, blank=True)
    tippani = models.ImageField(null=True, blank=True)
    voucher = models.ImageField(null=True, blank=True)
    debit_credit = models.ImageField(null=True, blank=True)
    quotation = models.ImageField(null=True, blank=True)
    memo = models.ImageField(null=True, blank=True)
    credit_note = models.ImageField(null=True, blank=True)
    approved_letter = models.ImageField(null=True, blank=True)


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



class PasswordReset(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField()
    key = models.CharField(max_length=50)
    changed = models.BooleanField(default=False)
    forced_expired = models.BooleanField(default=False)
    expires = models.IntegerField(default=2) # 2 days
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}'s passwrod reset".format(self.user.username)

    def regenerate(self):
        self.key = None
        self.save()

        if self.key is not None:
            return True
        return False

    def send_password_reset(self):
        if not self.changed and not self.forced_expired:
            context = {
                'path': 'localhost:8000/api/v1/email/reset-password/',
                'email': self.email,
            }

            if not self.key:
                key = random_string_generator(size=45)
            else:
                key = self.key
            txt = "{}{}".format(context.get('path'), key)
            html = "{}{}".format(context.get('path'), key)

            subject = "Password Reset"
            recipient_list = [self.email, ]

            sent_mail = send_mail(
                subject=subject,
                message=txt,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=recipient_list,
                html_message=html,
                fail_silently=False,
            )

            return sent_mail
        return False

def pre_save_password_reset(sender, instance, *args, **kwargs):
    if not instance.changed and not instance.forced_expired:
        if not instance.key:
            key = unique_key_generator(instance)
            instance.key = key

pre_save.connect(pre_save_password_reset, sender=PasswordReset)