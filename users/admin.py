from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('username', 'email', 'password1', 'password2')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)