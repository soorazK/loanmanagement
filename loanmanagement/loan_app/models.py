import json

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import pre_save
from nepali_date import NepaliDate

from .helpers import random_string_generator, unique_key_generator, LoanCalculator

# Default permissions for when a use is created
# If no permissions are specified, all permissions are set to False
DEFAULT_PERMISSIONS = {
    'loan': {
        'create': False,
        'retrieve': False,
        'update': False,
        'delete': False
    },
    'loantype': {
        'create': False,
        'retrieve': False,
        'update': False,
        'delete': False
    },
    'payment': {
        'create': False,
        'retrieve': False,
        'update': False,
        'delete': False
    },
    'user': {
        'create': False,
        'retrieve': False,
        'update': False,
        'delete': False
    },
}


# Create your models here.
class CustomUser(AbstractUser):
    """
    Extends Django's AbstractUser to create our own User model.
    Login, Logout and Authentication can be done with this model.
    """
    # Permissions field to store user's permissions on other models
    permissions = models.TextField(null=True, blank=True, default=json.dumps(DEFAULT_PERMISSIONS))

    # These fields are required when creating a new user along with username and password
    # :TODO: make email field a unique field
    REQUIRED_FIELDS = ['is_staff', 'email', 'permissions']

    def __str__(self):
        """
        String representation for the model object.
        :return: {str} User's username
        """
        return '{}'.format(self.username)


# Function to get the today's date in Bikram Sambat
def get_today_nepali_date():
    nepali_date_today = NepaliDate.today()
    return nepali_date_today.strfdate('%Y-%m-%d')


class Loantype(models.Model):
    """
    Store the details of Loan type.
    """
    loantype = models.CharField(max_length=100)
    interest = models.FloatField(default=0)
    period_years = models.FloatField(default=0.0)
    num_payments_per_year = models.FloatField(default=0.0)
    start_date = models.DateField(default=0.0)
    created_at = models.CharField(max_length=100, default=get_today_nepali_date())
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String representation of Loantype object.
        :return: {str} Type of loan
        """
        return self.loantype


def get_image_path(instance, filename):
    """
    Function to get the path for storing images

    :param instance: instance of a model
    :param filename: {str} name of uploaded file
    :return: {str} image path
    """
    return '{}/{}'.format(instance.employee_name, filename)


class Loan(models.Model):
    """
    Stores information about the loans.
    """
    # Choices for the loan's status
    STATUS_CHOICES = (
        ('DRAFTS', 'drafts'),
        ('STAGE ONE PENDING', 'stage_one_pending'),
        ('STAGE ONE VERIFIED', 'stage_one_verified'),
        ('STAGE TWO PENDING', 'stage_two_pending'),
        ('STAGE TWO VERIFIED', 'stage_two_verified'),
        ('ARCHIVED', 'archived'),
    )
    loanname = models.ForeignKey(Loantype, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    loanamount = models.DecimalField(max_digits=10, decimal_places=2)
    installment_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='DRAFTS')
    employee_id = models.IntegerField()
    permanent_address = models.CharField(max_length=100)
    temporary_address = models.CharField(max_length=100)
    DOB = models.DateField()
    recruitdate = models.DateField()

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

    position = models.CharField(max_length=100, blank=True)
    submission_form = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    lalpurja = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    malpot_receipt_1 = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    malpot_receipt_2 = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    verified_map = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    blue_print = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    committee_sifaris = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    marriage_certificate = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    mun_vdc_sifaris = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    dristibandha = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    close_house_photo = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    inspection_report = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    anusuchi_six_form = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    tippani = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    voucher = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    debit_credit = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    quotation = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    memo = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    credit_note = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    approved_letter = models.ImageField(upload_to=get_image_path, null=True, blank=True)

    # Loan Issue Details
    loan_issue_1_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    loan_issue_1_status = models.BooleanField(default=False)
    loan_issue_1_date = models.DateField(blank=True, null=True)

    loan_issue_2_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    loan_issue_2_status = models.BooleanField(default=False)
    loan_issue_2_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String representation of Loan model
        :return: {str}
        """
        return "{} - {} - {}".format(self.employee_name, self.loanname.loantype, self.status)


# Function that runs when Loan object is saved
# Used to calculate monthly installment amount according to loan amount, interest and other params
def pre_save_loan(sender, instance, *args, **kwargs):
    loant = instance.loanname
    lc = LoanCalculator(instance.loanamount, loant.interest, loant.period_years, loant.num_payments_per_year,
                        loant.start_date)

    instance.installment_amount = lc.payment_per_period


# Connect the pre_save_loan function with Django's signal
pre_save.connect(pre_save_loan, sender=Loan)


class Payment(models.Model):
    """
    Stores the information about Payment model.
    """
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    installment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    extra_payment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    payment_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String representation of Payment model
        :return: {str}
        """
        return "{}-{}".format(self.payment_amount, self.loan)


# Function that runs when payment object is saved
# Used to differentiate installment amount payment and extra payment from payment amount
def pre_save_payment(sender, instance, *args, **kwargs):
    installment_amount = instance.loan.installment_amount

    if instance.payment_amount > installment_amount:
        instance.installment = installment_amount
        instance.extra_payment = instance.payment_amount - installment_amount
    else:
        instance.installment = instance.payment_amount
        instance.extra_payment = 0


# Connect pre_save_payment function with Django's signal
pre_save.connect(pre_save_payment, sender=Payment)


# Section below this is not used currently
class PasswordReset(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField()
    key = models.CharField(max_length=50)
    changed = models.BooleanField(default=False)
    forced_expired = models.BooleanField(default=False)
    expires = models.IntegerField(default=2)  # 2 days
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
