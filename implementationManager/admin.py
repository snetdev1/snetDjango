from django.contrib import admin
from implementationManager.models import *

class userProInLine(admin.StackedInline):
    model = projectUser

class projectAdmin(admin.ModelAdmin):
    model = project

    inlines = [
        userProInLine,
    ]

admin.site.register(project, projectAdmin)

