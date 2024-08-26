from django.contrib import admin
from .models import *

class PeopleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'birth', 'member_rccg', 'whatsapp_no', 'referee', 'attended_prev', 'suggestions']
    search_fields = ['name', 'referee']
    list_filter = ['id']


admin.site.register(People, PeopleAdmin)
