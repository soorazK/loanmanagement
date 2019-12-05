from rest_framework import serializers
from ..models import Loantype,Loan,Payment

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields=[
        'pk',
        'loantype_id',
        'employee_name',
        'employee_id',
        'recruitdate',
        'position',
        'loanamount',
        'status',
        'permanent_address',
        'temporary_address',
        'DOB',
        ]

class LoantypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loantype
        fields=[
        'pk',
        'loantype',
        'interest',
        ]
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields=[
        'payment_amount',
        'loan_id',
        'payment_date',
        ]

""""
data= {
"employee_name":"sooraz"#,
"loanamaount":"40,000/-",
"publish":"2016-2-12",
}
new_item = LoanSerializer(data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)
"""
