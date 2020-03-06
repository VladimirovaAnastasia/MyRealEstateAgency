from django.contrib import admin

from .models import Flat
from .models import Complaint
from .models import Owner


class AdminFlat(admin.ModelAdmin):
    search_fields = ('id', 'town', 'address')
    readonly_fields = ['construction_year']
    list_display = ('id', 'address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ('new_building', 'town', 'price')
    raw_id_fields = ("users_who_likes",)


class AdminComplaint(admin.ModelAdmin):
    raw_id_fields = ("user", "flat")
    list_display = ('description', )


class AdminOwner(admin.ModelAdmin):
    raw_id_fields = ("owners_flats",)


admin.site.register(Flat, AdminFlat)
admin.site.register(Complaint, AdminComplaint)
admin.site.register(Owner, AdminOwner)
