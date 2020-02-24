from django.contrib import admin

from .models import Flat
from .models import Complaint


class AdminFlat(admin.ModelAdmin):
    search_fields = ('town', 'owner', 'address')
    readonly_fields = ['construction_year']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ('new_building', 'town', 'price')


class AdminComplaint(admin.ModelAdmin):
    raw_id_fields = ("user", "flat")


admin.site.register(Flat, AdminFlat)
admin.site.register(Complaint, AdminComplaint)
