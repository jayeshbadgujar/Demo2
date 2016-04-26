from django.contrib import admin

# Register your models here.
from .models import Quotation, Item


class EmployeeInline(admin.StackedInline):
    model = Item


class CompanyAdmin(admin.ModelAdmin):

    inlines = [
        EmployeeInline,
    ]

    model = Quotation


admin.site.register(Quotation)
admin.site.register(Item)

