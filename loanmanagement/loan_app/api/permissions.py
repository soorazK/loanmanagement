import json
from rest_framework import permissions

from ..models import CustomUser


class LoanCreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.get(username=request.user)
        perms = json.loads(user.permissions)
        perm = perms.get('loan').get('create')
        return perm


class LoanListRetrievePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.get(username=request.user)
        perms = json.loads(user.permissions)
        perm = perms.get('loan').get('retrieve')
        return perm


class LoanUpdatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.get(username=request.user)
        perms = json.loads(user.permissions)
        perm = perms.get('loan').get('update')
        return perm

class LoanDeletePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.get(username=request.user)
        perms = json.loads(user.permissions)
        perm = perms.get('loan').get('delete')
        return perm


class LoanTypeCreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.get(username=request.user)
        perms = json.loads(user.permissions)
        perm = perms.get('loantype').get('create')
        return perm


class LoanTypeListRetrievePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.get(username=request.user)
        perms = json.loads(user.permissions)
        perm = perms.get('loantype').get('retrieve')
        return perm


class LoanTypeUpdatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.get(username=request.user)
        perms = json.loads(user.permissions)
        perm = perms.get('loantype').get('update')
        return perm


class LoanTypeDeletePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.get(username=request.user)
        perms = json.loads(user.permissions)
        perm = perms.get('loantype').get('delete')
        return perm


class PaymentCreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.get(username=request.user)
        perms = json.loads(user.permissions)
        perm = perms.get('payment').get('create')
        return perm


class PaymentListRetrievePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.get(username=request.user)
        perms = json.loads(user.permissions)
        perm = perms.get('payment').get('retrieve')
        return perm


class PaymentUpdatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.get(username=request.user)
        perms = json.loads(user.permissions)
        perm = perms.get('payment').get('update')
        return perm


class PaymentDeletePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.get(username=request.user)
        perms = json.loads(user.permissions)
        perm = perms.get('payment').get('delete')
        return perm


class UserCreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.get(username=request.user)
        perms = json.loads(user.permissions)
        perm = perms.get('user').get('create')
        return perm


class UserListRetrievePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.get(username=request.user)
        perms = json.loads(user.permissions)
        perm = perms.get('user').get('retrieve')
        return perm


class UserUpdatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.get(username=request.user)
        perms = json.loads(user.permissions)
        perm = perms.get('user').get('update')
        return perm


class UserDeletePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.get(username=request.user)
        perms = json.loads(user.permissions)
        perm = perms.get('user').get('delete')
        return perm