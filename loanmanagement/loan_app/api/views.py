from rest_framework.generics import (ListAPIView,
RetrieveAPIView,
UpdateAPIView,
DestroyAPIView,
CreateAPIView)

from django.http import HttpResponse
import datetime as dt

from copy import deepcopy
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from  ..models import Loantype,Loan,Payment, CustomUser, PasswordReset, DEFAULT_PERMISSIONS
from .serializers import LoanSerializer,LoanListSerializer,LoantypeSerializer,PaymentSerializer, LoginSerializer, UserSerializer,PaymentListSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter

import json
from django_filters.rest_framework import DjangoFilterBackend
from ..helpers import convert_to_present_value

from ..helpers import LoanCalculator, render_to_pdf, fetch_resources
from .permissions import (
    LoanCreatePermission, LoanListRetrievePermission, LoanUpdatePermission, LoanDeletePermission,
    LoanTypeCreatePermission, LoanTypeListRetrievePermission, LoanTypeUpdatePermission, LoanTypeDeletePermission,
    PaymentCreatePermission, PaymentListRetrievePermission, PaymentUpdatePermission, PaymentDeletePermission,
    UserCreatePermission, UserListRetrievePermission, UserUpdatePermission, UserDeletePermission,
)

#api for loan


# class LoanView(APIView):
#     parser_classes = (FileUploadParser, )
#     def post(self, request, *args, **kwargs):
#         loan_serializer = LoanSerializer(data=request.data)
#
#         if loan_serializer.is_valid():
#             loan_serializer.save()
#             return Response(loan_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(loan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoanlistAPIView(ListAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [LoanListRetrievePermission]
    queryset=Loan.objects.all()
    serializer_class=LoanListSerializer
    #pagination_class=LoanLimitOffsetPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ['status']
    search_fields = ('status', 'employee_id', 'employee_name')

class LoanDetailAPIView(RetrieveAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [LoanListRetrievePermission]
    queryset=Loan.objects.all()
    serializer_class=LoanListSerializer
    lookup_field='pk'
    #lookup_url_kwarg==

class LoanUpdateAPIView(UpdateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [LoanUpdatePermission]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoanDeleteAPIView(DestroyAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [LoanDeletePermission]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoanCreateAPIView(CreateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [LoanCreatePermission]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==
#api for loantype

class LoantypelistAPIView(ListAPIView):
    authentication_classes = ()
    # permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer

class LoantypeDetailAPIView(RetrieveAPIView):
    authentication_classes = ()
    # permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoantypeUpdateAPIView(UpdateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [LoanTypeUpdatePermission]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoantypeDeleteAPIView(DestroyAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [LoanTypeDeletePermission]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoantypeCreateAPIView(CreateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [LoanTypeCreatePermission]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer

#api for payment
class PaymentlistAPIView(ListAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [PaymentListRetrievePermission]
    queryset=Payment.objects.all()
    serializer_class=PaymentListSerializer

class PaymentDetailAPIView(RetrieveAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [PaymentListRetrievePermission]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    #lookup_field=
    #lookup_url_kwarg==

class PaymentUpdateAPIView(UpdateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [PaymentUpdatePermission]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    #lookup_field=
    #lookup_url_kwarg==

class PaymentDeleteAPIView(DestroyAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [PaymentDeletePermission]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    #lookup_field=
    #lookup_url_kwarg==

class PaymentCreateAPIView(CreateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [PaymentCreatePermission]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer


class LoginView(APIView):
    authentication_classes = ()
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        username = user.username
        user_perms = json.loads(user.permissions)

        token, created = Token.objects.get_or_create(user=user)

        if created:
            return Response({"token": token.key, 'username': username, 'permissions': user_perms}, status=201)
        else:
            token.delete()
            new_token = Token.objects.create(user=user)
            return Response({'token': new_token.key, 'username': username, 'permissions': user_perms}, status=200)

class UserList(ListAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [UserListRetrievePermission]

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserAddAPIView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [UserCreatePermission]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_exists = CustomUser.objects.filter(username=serializer.validated_data['username']).exists()

        if user_exists:
            return Response({'msg': 'Username already taken'}, status=409)

        try:
            input_permissions = request.data.get('permissions', {})
            loan_perms = input_permissions.get('loan', {})
            loantype_perms = input_permissions.get('loantype', {})
            payment_perms = input_permissions.get('payment', {})
            user_perms = input_permissions.get('user', {})

            new_permissions = deepcopy(DEFAULT_PERMISSIONS)
            new_permissions.get('loan', {}).update(loan_perms)
            new_permissions.get('loantype', {}).update(loantype_perms)
            new_permissions.get('payment', {}).update(payment_perms)
            new_permissions.get('user', {}).update(user_perms)

            new_permissions = json.dumps(new_permissions)
        except Exception as e:
            return Response({'msg': 'Permission should be in JSON'}, status=400)

        user = CustomUser(
            username = serializer.validated_data['username'],
            email = serializer.validated_data['email'],
            first_name = serializer.validated_data.get('first_name', ''),
            last_name = serializer.validated_data.get('last_name', ''),
            is_staff = serializer.validated_data.get('is_staff', False),
            permissions = new_permissions,
        )

        user.set_password(serializer.validated_data['password'])

        user.save()

        return Response({'msg': 'User created successfully'}, status=201)


class UserUpdateAPIView(UpdateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [UserUpdatePermission]
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer

    def post(self, request, username):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        current_user = CustomUser.objects.get(username=username)
        if not current_user:
            return Response({'msg': "Not found"}, status=400)

        password = serializer.validated_data.get('password')
        first_name = serializer.validated_data.get('first_name')
        last_name = serializer.validated_data.get('last_name')
        email = serializer.validated_data.get('email')
        is_staff = serializer.validated_data.get('is_staff')

        permissions = request.data.get('permissions', {})

        current_permissions = current_user.permissions

        try:
            current_permissions = json.loads(current_permissions)
            loan_perms = permissions.get('loan', {})
            loantype_perms = permissions.get('loantype', {})
            payment_perms = permissions.get('payment', {})
            user_perms = permissions.get('user_perms', {})

            current_permissions.get('loan').update(loan_perms)
            current_permissions.get('loantype').update(loantype_perms)
            current_permissions.get('payment').update(payment_perms)
            current_permissions.get('user').update(user_perms)
            current_permissions = json.dumps(current_permissions)
        except Exception as e:
            return Response({'msg': 'Permission is not valid'}, status=400)


        current_user.first_name = first_name or current_user.first_name
        current_user.last_name = last_name or current_user.last_name
        current_user.email = email or current_user.email
        current_user.is_staff = current_user.is_staff if is_staff is None else is_staff
        current_user.permissions = current_permissions

        if password:
            current_user.set_password(password)

        current_user.save()

        return Response({"msg": "success"}, status=201)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        try:
            user = request.user
            token = Token.objects.get(user=user)
            token.delete()
            return Response({'msg': 'Logout Successful'}, status=200)
        except Exception as e:
            return Response({'msg': 'Logout Failed'}, status=500)

class SendPasswordReset(APIView):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]

    def send_password_reset_email(self, user):
        pass_reset = PasswordReset(user=user, email=user.email)
        pass_reset.save()

        result = pass_reset.send_password_reset()

        if result is False:
            return Response({'msg': 'Password Reset Email could not be sent'}, status=500)
        return Response({'msg': 'Password Reset Email sent.'}, status=200)

    def post(self, request, slug):

        users = CustomUser.objects.filter(username=slug)

        if len(users) <= 0:
            return Response({'msg': 'User not found'}, status=404)

        user = users[0]

        prs = PasswordReset.objects.filter(user=user)

        if len(prs) <= 0:
            return self.send_password_reset_email(user)
        else:
            for pr in prs:
                pr.forced_expired = True
                pr.save()

            return self.send_password_reset_email(user)


class ResetPassword(APIView):
    def get(self, request, slug):

        pass_reset = PasswordReset.objects.filter(key=slug)

        if len(pass_reset) <= 0:
            return Response({'msg': 'Request url not found'}, status=400)

        pr = pass_reset[0]

        if not pr.changed and not pr.forced_expired:
            new_password = request.data['new_password']

            user = pr.user

            user.set_password(new_password)
            user.save()
            pr.changed = True
            pr.save()

            return Response({'msg': 'Password changed'}, status=200)
        else:
            return Response({'msg': 'This url has already been used.'}, status=300)


class CheckToken(APIView):
    authentication_classes = ()

    def post(self, request):
        key = request.data.get('token')

        if key:
            try:
                token = Token.objects.get(key=key)

                user = CustomUser.objects.get(username=token.user.username)

                permissions = json.loads(user.permissions)

                return Response({'msg': 'Authentication Token found', 'username': token.user.username, "permissions":permissions}, status=200)
            except:
                return Response({'msg': 'Authentication Token not found', 'username': '', "permissions": {}}, status=404)
        return Response({'msg': 'Authentication Token not supplied', 'username': '', "permissions": {}}, status=400)


class LoanCalculatorView(APIView):
    authentication_classes = ()

    def post(self, request):
        WEEKS_IN_YR = 52
        DAYS_IN_YR = 365
        loan_type = request.data.get('loan_type')
        loan_amount = request.data.get('loan_amount')
        retirement_date = request.data.get('retirement_date')


        if not loan_type or not loan_amount or not retirement_date:
            return Response({'msg': 'Required information is missing'}, status=400)

        try:
            retirement_date = dt.date.fromisoformat(retirement_date)
        except:
            return Response({'msg': 'Retirement date format mismatch'}, status=400)

        try:
            loantype = Loantype.objects.get(loantype=loan_type)
            today_date = dt.date.today()
            if today_date + dt.timedelta(weeks=loantype.period_years*WEEKS_IN_YR) > retirement_date:
                period_years = (retirement_date - today_date).days / DAYS_IN_YR

            else:
                period_years = loantype.period_years
            lc = LoanCalculator(loan_amount, loantype.interest, period_years, loantype.num_payments_per_year, loantype.start_date)
            breakdown = lc.generate_table()

            return Response({'msg': 'Success', 'breakdown': breakdown}, status=200)
        except Exception as e:
            return Response({'msg': 'Some error occured'}, status=500)


class GetLoanDetail(APIView):
    authentication_classes = ()

    def post(self, request):
        loan_type = request.data.get('loan_type')
        dob = request.data.get('dob')
        loan_amount = request.data.get('loan_amount')
        # mobile_number = request.data.get('mobile_number')

        if not dob or not loan_amount or not loan_type: #or not mobile_number
            return Response({'msg': 'Required information is missing'}, status=400)

        try:
            loan = Loan.objects.get(loanname__loantype=loan_type, DOB=dob, loanamount=loan_amount) #, employee_name=employee_name, mobile_number=mobile_number)
            serializer = LoanSerializer(loan)

            retirement_date = loan.retirement_date
            loan_start_date = loan.loan_issue_1_date

            if loan_start_date is None:
                return Response({'msg': 'Success', 'loan_detail': serializer.data, 'breakdown': [], 'payment_details': []}, status=200)

            today_date = dt.date.today()
            elapsed_time = (today_date - loan_start_date).days / 365
            period_years = loan.loanname.period_years - elapsed_time
            if today_date + dt.timedelta(weeks=period_years * 52) > retirement_date:
                period_years = (loan.retirement_date - today_date).days / 365
            else:
                period_years = period_years
            rate = loan.loanname.interest
            if not loan.loan_issue_1_status:
                breakdown = []
            else:
                issue_1_amount = loan.loan_issue_1_amount
                issue_1_date = loan.loan_issue_1_date

                issue_1_period = (today_date - issue_1_date).days / 365
                issue_1_present_val = convert_to_present_value({'rate': rate, 'principle': issue_1_amount, 'time': issue_1_period})

                if loan.loan_issue_2_status:
                    issue_2_amount = loan.loan_issue_2_amount
                    issue_2_date = loan.loan_issue_2_date
                    issue_2_period = (today_date - issue_2_date).days / 365

                    issue_2_present_val = convert_to_present_value({'rate': rate, 'principle': issue_2_amount, 'time': issue_2_period})
                    issues_present_val = issue_1_present_val + issue_2_present_val
                else:
                    issues_present_val = issue_1_present_val

            payments = loan.payment_set.all().order_by('-updated_on')

            payments_present_val = 0
            for payment in payments:
                payment_amount = payment.payment_amount
                payment_date = payment.payment_date
                payment_period = (today_date - payment_date).days / 365
                payment_present_val = convert_to_present_value({'rate': rate, 'principle': payment_amount, 'time': payment_period})
                payments_present_val += payment_present_val

            new_loan_amount = issues_present_val - payments_present_val
            payment_serializer = PaymentListSerializer(payments, many=True)
            lc = LoanCalculator(new_loan_amount, rate, period_years, loan.loanname.num_payments_per_year, loan.loanname.start_date)
            breakdown = lc.generate_table()

            return Response({'msg': 'Success', 'loan_detail':serializer.data, 'breakdown': breakdown, 'payment_details': payment_serializer.data}, status=200)
        except Exception as e:
            return Response({'msg': 'Loan not found', 'loan_detail': {}, 'breakdown': {}}, status=404)



class GetAnalytics(APIView):
    authentication_classes = (TokenAuthentication, )

    def get(self, request):
        response_schema = {
            'msg': '',
            'analytics': {
                'pie_chart': [

                ],
                'line_chart': [

                ],
                'bar_chart': [

                ],
                'forcast_chart': [

                ]
            },
        }

        try:
            today = dt.date.today()
            current_year = today.year
            current_month = today.month

            if current_month == 12:
                start_year = current_year
                start_month = 1
                check_at = [(start_year, i) for i in range(1, current_month + 1)]
            else:
                start_year = current_year - 1
                start_month = current_month + 1
                check_at = [(start_year, i) for i in range(start_month, 13)]
                check_at.extend([(current_year, i) for i in range(1, current_month + 1)])

            loan_types = Loantype.objects.all()

            for loan_type in loan_types:
                payment_collection_this_month = 0
                loan_issued_this_month = 0
                loans = loan_type.loan_set.all()
                for loan in loans:
                    if loan.loan_issue_1_status and loan.loan_issue_1_date.year == current_year and loan.loan_issue_1_date.month == current_month:
                        loan_issued_this_month += loan.loan_issue_1_amount
                    if loan.loan_issue_2_status and loan.loan_issue_2_date.year == current_year and loan.loan_issue_2_date.month == current_month:
                        loan_issued_this_month += loan.loan_issue_2_amount

                    payments = loan.payment_set.all()
                    for payment in payments:
                        if payment.payment_date.year == current_year and payment.payment_date.month == current_month:
                            payment_collection_this_month += payment.payment_amount

                try:
                    forecast_amount = loan.installment_amount
                except:
                    forecast_amount = 0
                response_schema.get('analytics').get('bar_chart').append({'name': loan_type.loantype, 'Loan issued last month': loan_issued_this_month})
                response_schema.get('analytics').get('pie_chart').append({'name': loan_type.loantype, 'value':payment_collection_this_month})
                response_schema.get('analytics').get('forcast_chart').append({'name': loan_type.loantype, 'Payment Forecast': forecast_amount})



            for check in check_at:
                month_name = "{}-{}".format(check[0], check[1])
                final_json = {'name': month_name}
                for loan_type in Loantype.objects.all():
                    payments = Payment.objects.filter(loan__loanname__loantype=loan_type, payment_date__year=check[0], payment_date__month=check[1])
                    total_payment_for_checked_month = 0
                    for payment in payments:
                        total_payment_for_checked_month += payment.payment_amount

                    final_json.update({loan_type.loantype: total_payment_for_checked_month})

                response_schema.get('analytics').get('line_chart').append(final_json)
                response_schema['msg'] = 'Success'
            return Response(response_schema, status=200)
        except Exception as e:
            return Response({'msg': 'Failure', 'analytics': {}}, status=500)


class CheckPassword(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        password = request.data.get('password')

        if not password:
            return Response({'msg': 'Required field missing'}, status=400)

        user = CustomUser.objects.get(username=request.user)

        if not user.check_password(password):
            return Response({'msg': 'Incorrect Password'}, status=412)

        return Response({'msg': 'Accepted'}, status=200)


class TestView(APIView):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [NewPermission]

    def get(self, request):
        loan = Loan.objects.get(pk=1)

        context = {
            "loan": loan
        }
        pdf = render_to_pdf('dashboard.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Trial.pdf"
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
