from django.contrib import admin

from .models import * # Import all of models

admin.site.register(Customer) # Now you can see Customer in admin panel
admin.site.register(Product) 
admin.site.register(Order)
admin.site.register(Tag)  