from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User
from .forms import UserChangeForm, UserCreationForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    form =UserChangeForm
    add_form = UserCreationForm
    list_display = ['username', "is_admin"]
    list_filter = ["is_admin"]

    fieldsets = (
        (None, {'fields':('username','password')}),
    )

    add_fieldsets = (
        (None, {'fields':('username','password1', 'password2')}),
    )

    filter_horizontal = []

admin.site.register(User, CustomUserAdmin)
# admin.site.unregister(Group)