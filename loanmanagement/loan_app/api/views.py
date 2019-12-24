from rest_framework.generics import (ListAPIView,
RetrieveAPIView,
UpdateAPIView,
DestroyAPIView,
CreateAPIView)

from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from  ..models import Loantype,Loan,Payment, CustomUser, PasswordReset
from .serializers import LoanSerializer,LoantypeSerializer,PaymentSerializer, LoginSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter

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
    permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #pagination_class=LoanLimitOffsetPagination
    filter_backends = (SearchFilter, )
    search_fields = ('status', 'employee_id', 'employee_name')

class LoanDetailAPIView(RetrieveAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    lookup_field='employee_id'
    #lookup_url_kwarg==

class LoanUpdateAPIView(UpdateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoanDeleteAPIView(DestroyAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoanCreateAPIView(CreateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==
#api for loantype

class LoantypelistAPIView(ListAPIView):
    authentication_classes = ()
    permission_classes = [IsAuthenticated]
    #queryset=Loantype.objects.all()
    #queryset.filter(loantype="motorcycle loan")
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
    #filterset_class = LoantypelistFilterSet
    #def get_queryset(self):

    #    a=queryset.exclude('pk')
    #    return queryset
    #exclude=('created_on',)
    #filter_backends = (filters.DjangoFilterBackend,)
    #filterset_fields = ('created_on')

class LoantypeDetailAPIView(RetrieveAPIView):
    authentication_classes = ()
    permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoantypeUpdateAPIView(UpdateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoantypeDeleteAPIView(DestroyAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoantypeCreateAPIView(CreateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer

class PaymentlistAPIView(ListAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer

class PaymentDetailAPIView(RetrieveAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    #lookup_field=
    #lookup_url_kwarg==

class PaymentUpdateAPIView(UpdateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    #lookup_field=
    #lookup_url_kwarg==

class PaymentDeleteAPIView(DestroyAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    #lookup_field=
    #lookup_url_kwarg==

class PaymentCreateAPIView(CreateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer


class LoginView(APIView):
    authentication_classes = ()
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        django_login(request, user)

        token, created = Token.objects.get_or_create(user=user)

        if created:
            return Response({"token": token.key}, status=200)
        else:
            token.delete()
            new_token = Token.objects.create(user=user)
            return Response({'token': new_token.key}, status=200)

class UserAddAPIView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_exists = CustomUser.objects.filter(username=serializer.validated_data['username']).exists()

        if user_exists:
            return Response({'msg': 'Username already taken'}, status=409)

        user = CustomUser(
            username = serializer.validated_data['username'],
            email = serializer.validated_data['email'],
            first_name = serializer.validated_data.get('first_name', ''),
            last_name = serializer.validated_data.get('last_name', ''),
            is_staff = serializer.validated_data.get('is_staff', False)
        )

        user.set_password(serializer.validated_data['password'])

        user.save()

        return Response({'msg': 'User created successfully'}, status=201)


class UserUpdateAPIView(UpdateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAdminUser]
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

        current_user.first_name = first_name or current_user.first_name
        current_user.last_name = last_name or current_user.last_name
        current_user.email = email or current_user.email
        current_user.is_staff = current_user.is_staff if is_staff is None else is_staff

        if password:
            current_user.set_password(password)

        current_user.save()

        return Response({"msg": "success"}, status=201)


class LogoutView(APIView):
    authentication_classes = ()
    def post(self, request):
        try:
            django_logout(request)
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
                return Response({'msg': 'Authentication Token found', 'username': token.user.username}, status=200)
            except:
                return Response({'msg': 'Authentication Token not found', 'username': ''}, status=404)
        return Response({'msg': 'Authentication Token not supplied', 'username': ''}, status=400)
