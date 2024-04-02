
# Register your models here.

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_of_birth',
                    'user_image', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'date_of_birth', 'password')}),
        ('Personal info', {'fields': ('user_image',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff',

         'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),

            'fields': ('username', 'email', 'date_of_birth', 'password1', 'password2'),
        }),


        {'fields': ('username', 'email', 'date_of_birth', 'user_image', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
         }),

    search_fields = ('email', 'username')
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
