from django.contrib import admin
from .models import Menu, Order, Table, TableBooking

admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Table)
admin.site.register(TableBooking)
