from django.contrib import admin
from .models import CustomUser, Manager, Client


admin.site.register(CustomUser)
# admin.site.register(Manager)
admin.site.register(Client)




class ManagerAdmin(admin.ModelAdmin):

    list_display = (
        'first_name',
        'last_name',
        'email', 
        'successful_deals', 
        'phone_number',
        'created_at'
        )
    list_editable = (
        'first_name',
        'last_name',
        'email', 
        'successful_deals', 
        'phone_number'
        )
    # list_display_links = ('apartment_number', 'object_name', 'floor', 'square_meters')
    list_display_links = None
    # list_filter = ('status',)
    search_fields = ('email',)


admin.site.register(Manager, ManagerAdmin)
