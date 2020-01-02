from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Loan,Loantype, CustomUser, Payment

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    fieldsets = (
        (None, {'fields': ('password', )}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}), (None, {'fields': ('permissions',)})
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_staff', 'permissions')}),
    )
    list_display = ['email', 'username', 'is_staff', 'permissions']


admin.site.site_header = "M-Tech Admin"
admin.site.site_title = "M-Tech Admin Portal"
admin.site.index_title = "Welcome to M-Tech Admin Portal"
admin.site.unregister(Group)
admin.site.register(Loan)
admin.site.register(Loantype)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Payment)
