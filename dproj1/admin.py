#from django.contrib import admin
#from .models import *

# Register your models here.
#admin.site.register(home)
#admin.site.register(process)
#from django.contrib import admin
#from .models import Homes


#admin.site.register(Homes)
#from django.contrib import admin
#from .models import Persondetails
#from .models import UserProfile
#from .models import OTPModel
#it is used to make the field column in the homes database.
#class PersondetailsAdmin(admin.ModelAdmin):
 #   list_display = ('username', 'password', 'email')  # Display these fields as columns

#admin.site.register(Persondetails, PersondetailsAdmin)

#class userprofileAdmin(admin.ModelAdmin):
 #   list_display =('user','profile_image','address','city','state','postal-code')

#admin.site.register('userprofile',userprofileAdmin)


#class UserProfileAdmin(admin.ModelAdmin):
 #   list_display = ('user', 'get_username', 'city', 'state', 'postal_code')
  #  search_fields = ('user__username', 'city', 'state', 'postal_code')
   # list_filter = ('city', 'state')

    #def get_username(self, obj):
     #   return obj.user.username
    #get_username.short_description = 'Username'

#admin.site.register(UserProfile, UserProfileAdmin)


#@admin.register(OTPModel)
#class OTPModelAdmin(admin.ModelAdmin):
 #   list_display = ('user', 'otp', 'created_at')
  #  search_fields = ('user__email',)  # Enables searching by user's email
   # list_filter = ('created_at',)  # Enables filtering by creation date
    #ordering = ('-created_at',)  # Orders entries by creation date, newest first

   #return f"{obj.otp[:3]}***"\
   #class OTPModelAdmin(admin.ModelAdmin):
    #list_display = ('user', 'display_otp', 'created_at')

    #def display_otp(self, obj):
     #   return f"{obj.otp[:3]}***"
    #display_otp.short_description = 'OTP'  # Custom column header

    #search_fields = ('user__email',)
    #list_filter = ('created_at',)
    #ordering = ('-created_at',)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Persondetails

class PersondetailsAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')  
    search_fields = ('username', 'email')  
    readonly_fields = ('date_joined', 'last_login')  

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    actions = ['delete_selected'] 


    def delete_selected(self, request, queryset):
        count = queryset.count()
        queryset.delete()  
        self.message_user(request, f'Deleted {count} user(s) successfully.')

    delete_selected.short_description = "Delete selected users"  
admin.site.register(Persondetails, PersondetailsAdmin)







