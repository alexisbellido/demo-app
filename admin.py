from django.contrib import admin

from .models import Article, TVProgram


class TVProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time')

admin.site.register(TVProgram, TVProgramAdmin)

admin.site.register(Article)
