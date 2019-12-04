from django.contrib import admin

from .models import Loan, Loantype

# Register your models here.
admin.site.register(Loan)
admin.site.register(Loantype)