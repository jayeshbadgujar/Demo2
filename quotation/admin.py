from django.contrib import admin

# Register your models here.
from .models import Quotation, Item





admin.site.register(Quotation)
admin.site.register(Item)

