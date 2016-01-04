from django.contrib import admin
from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'email'
    ]

    readonly_fields = [
        'password',
        'date_joined',
        'last_login',
        'created_at',
        'updated_at'
    ]

admin.site.register(User, UserAdmin)
