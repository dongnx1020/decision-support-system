from django.contrib import admin
from dashboard.models import Customer, TotalMoneyCategory, ClusterCenter, ClusterCustomer

# Register your models here.

admin.site.register(Customer)
admin.site.register(TotalMoneyCategory)
admin.site.register(ClusterCenter)
admin.site.register(ClusterCustomer)