from django.contrib import admin

from .models import pro_details
from .models import products

# Register your models here.

admin.site.register(pro_details),
admin.site.register(products),

