from django.contrib import admin

from .models import Flat


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('town', 'owner', 'address')
    readonly_fields = ["construction_year"]


admin.site.register(Flat, AuthorAdmin)
