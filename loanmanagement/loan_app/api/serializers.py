from rest_framework import serializers
from ..models import Loantype,Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields=[
        'employee_name',
        'loanamount',
        'status',
        ]

class LoantypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loantype
        fields=[
        'type',
        'interest',
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
