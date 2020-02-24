from django.contrib import admin

from .models import Flat


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('town', 'owner', 'address')
    readonly_fields = ['construction_year']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']




admin.site.register(Flat, AuthorAdmin)
