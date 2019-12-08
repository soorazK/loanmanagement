from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from .helpers import LoanCalculator
from .models import Loantype, Loan, Payment

# Create your views here.
#def logo_change(request):
#if(request.method == 'POST'):

#return render (request,'abc.html',context)
def dashboard(request):
    context = {}

    return render(request, 'dashboard.html', context)

# :TODO: to removed, for dev test only
@csrf_exempt
def loan_calculator_test(request):
    if request.method == 'POST':
        #loan_id = int(request.POST(['loan_id']))
        loan_obj = Loan.objects.get(loanname=3)
        loancal = LoanCalculator(loan_obj.loanamount, loan_obj.loanname.interest, loan_obj.loanname.period_years, loan_obj.loanname.num_payments_per_year, 'x')
        return JsonResponse({"cashflow": loancal.generate_table()})
    else:
        # :TODO: to changed with proper error code
        return JsonResponse({'error': 'Method not Allowed'})

def formtest(request):
    context = {}
    return render(request, 'form.html', context)


# :TODO: to removed, for dev test only
@csrf_exempt
def check_payments(request):
    if request.method == 'POST':
        loan_id = int(request.POST['loan_id'])
        loan_obj = Loan.objects.get(loantype_id=loan_id)
        payments = loan_obj.payment_set.all()

        in_json = serializers.serialize('json', payments)
        return JsonResponse({"payments": in_json})
    else:
        # :TODO: to changed with proper error code
        return JsonResponse({'error': 'Method not allowed.'})
