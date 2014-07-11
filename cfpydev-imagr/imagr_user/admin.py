from django.contrib import admin
from imagr_user.models import ImagrUser

class ImagrUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ['username', 'first_name', 'last_name', 'email']


admin.site.register(ImagrUser, ImagrUserAdmin)