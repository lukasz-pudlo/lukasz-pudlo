from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = ((None, {"fields": ("email", "password")}), *DjangoUserAdmin.fieldsets[2:])
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),)
    list_display = ["email", "is_staff", "is_superuser"]
    search_fields = ["email"]
    ordering = ["email"]
    readonly_fields = ["last_login", "date_joined"]
