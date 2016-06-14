from django.contrib import admin

from here.models import *


class partyAdmin(admin.ModelAdmin):
    model = party


admin.site.register(party, partyAdmin)
