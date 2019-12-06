from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .helpers import LoanCalculator
from .models import Loantype, Loan, Payment

# Create your views here.


def dashboard(request):
    context = {}

    return render(request, 'dashboard.html', context)

@csrf_exempt
def loan_calculator_test(request):
    if request.method == 'POST':
        loan_id = int(request.POST['loan_id'])
        loan_obj = Loan.objects.get(loantype_id=loan_id)
        loancal = LoanCalculator(loan_obj.loanamount, loan_obj.loantype_id.interest, loan_obj.loantype_id.period_years, loan_obj.loantype_id.num_payments_per_year, 'x')
        return JsonResponse({"cashflow": loancal.generate_table()})
    else:
        return JsonResponse({'error': 'Method not Allowed'})

def formtest(request):
    context = {}
    return render(request, 'form.html', context)
