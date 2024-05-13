from django.contrib import admin
from .models import Pizza, Topping, Order, Review

# Register your models here.


admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Order)
admin.site.register(Review)