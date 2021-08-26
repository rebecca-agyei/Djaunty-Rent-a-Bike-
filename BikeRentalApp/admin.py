from django.contrib import admin
from .models import Bike, Renter, Rental

# Register your models here.
admin.site.register(Bike)
admin.site.register(Renter)
admin.site.register(Rental)
