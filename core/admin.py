from django.contrib import admin

# Register your models here.

from .models import MenuItem, Reservation

admin.site.register(MenuItem)
admin.site.register(Reservation)
