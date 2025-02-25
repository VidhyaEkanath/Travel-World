from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Userregistration)
admin.site.register(Vendorregistration)
admin.site.register(Booknow)

@admin.register(Package)
class Packageadmin(admin.ModelAdmin):
    actions = ["approve_package"]
    def approve_package(self , request , queryset) :
        queryset.update(is_approved = True)