from django.contrib import admin

from core.models import *


class cmsAdmin(admin.ModelAdmin):
    model = cms


admin.site.register(cms, cmsAdmin)
