from django.contrib import admin
from .models import NewUser

# Register your models here.


class NewUserAdmin(admin.ModelAdmin):
    list_display = ('username','date_joined', 'profile')


admin.site.register(NewUser, NewUserAdmin)