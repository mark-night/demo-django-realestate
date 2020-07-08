from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'name',
                    'email', 'phone', 'message', 'contact_date')
    list_display_links = ('id', 'listing', 'name', 'email', 'message')
    search_fields = ('listing', 'name', 'email')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
