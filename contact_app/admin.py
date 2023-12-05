from django.contrib import admin

from .models import *

class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'manzil_title', 'manzil_body']
admin.site.register(AboutMe, AboutMeAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'message']
admin.site.register(Message, MessageAdmin)