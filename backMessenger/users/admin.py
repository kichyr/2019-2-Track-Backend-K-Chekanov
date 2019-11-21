from django.contrib import admin
from users.models import User, Member, Attachment
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('login','first_name', 'last_name')
    
admin.site.register(User, UserAdmin)
