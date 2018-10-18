from django.contrib import admin

# Register your models here.
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo', 'status','RegistrationID','Profile_type','Sex_Type','Career','Exclusive_Club','Other_Clubs','Description']

admin.site.register(Profile, ProfileAdmin)