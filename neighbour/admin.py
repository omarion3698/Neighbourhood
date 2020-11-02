from django.contrib import admin
from .models import Neighbourhood, Healthservices, Notifications, Business, Health, Authorities, BlogPost, Profile


class HealthAdmin(admin.ModelAdmin):
    filter_horizontal =['Healthservices']

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Health,HealthAdmin)
admin.site.register(Business)
admin.site.register(Healthservices)
admin.site.register(Authorities)
admin.site.register(BlogPost)
admin.site.register(Profile)
admin.site.register(Notifications)