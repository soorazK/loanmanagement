from rest_framework import serializers
from rest_framework import exceptions
from django.contrib.auth import authenticate
from ..models import Loantype,Loan,Payment, CustomUser

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields=[
        'loanname',
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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields=[
            'first_name',
            'last_name',
            'password',
            'email',
        ]
        extra_kwargs = {'password': {'write_only': True}}


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username', '')
        password = data.get('password', '')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if  user.is_active:
                    data['user'] = user
                else:
                    msg = "User is inactive"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Invalid credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Either username or password is missing."
            raise exceptions.ValidationError(msg)

        return data


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
