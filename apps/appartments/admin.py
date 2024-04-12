from django.contrib import admin
from .models import Apartment



class ApartmentAdmin(admin.ModelAdmin):

    list_display = (
        'apartment_number', 
        'object_name', 
        'floor',
        'square_meters',
        'status',
        'price',
        'client',
        'purchase_date',
        'reservation_until'
        )
    list_editable = (
        'apartment_number', 
        'object_name', 
        'floor',
        'square_meters',
        'status',
        'price',
        'client',
        'purchase_date',
        'reservation_until'
        )
    # list_display_links = ('apartment_number', 'object_name', 'floor', 'square_meters')
    list_display_links = None
    list_filter = ('status',)
    search_fields = ('apartment_number','price')


admin.site.register(Apartment, ApartmentAdmin)





'''

    apartment_number
    object_name
    floor
    square_meters
    status
    price
    client
    purchase_date
    reservation_until
'''