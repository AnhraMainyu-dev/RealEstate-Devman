from django.contrib import admin

from .models import Flat

class FlatAdmin(admin.ModelAdmin):
    search_fields = ['address', 'owner', 'town']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'town', 'new_building', 'construction_year']
    list_editable = ['new_building']

admin.site.register(Flat, FlatAdmin)