from rest_framework import serializers
from ..models import Loantype,Loan,Payment

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields=[
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
        'recruitdate',
        'lalpurja',
        'malpot_receipt_1',
        'malpot_receipt_2',
        'verified_map',
        'blue_print',
        'committee_sifaris',
        'marriage_certificate',
        'mun_vdc_sifaris',
        'dristibandha',
        'close_house_photo',
        'inspection_report',
        'anusuchi_six_form',
        'submission_form',
        'voucher',
        'debit_credit',
        'quotation',
        'memo',
        'credit_note',
        'approved_letter'
        ]

class LoantypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loantype
        fields=[
        'pk',
        'loantype',
        'interest',
        'period_years',
        'num_payments_per_year',
        'start_date',
        'created_on',
        ]
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields=[
        'payment_amount',
        'loan',
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
