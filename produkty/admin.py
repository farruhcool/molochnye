from django.contrib import admin
from .models import *


class ProduktImageInline(admin.TabularInline):
    model = ProduktImage
    extra = 0
class ProduktAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Produkt._meta.fields]
    inlines = [ProduktImageInline]
    class Meta:
        model=Produkt
admin.site.register(Produkt, ProduktAdmin)

class ProduktImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProduktImage._meta.fields]

    class Meta:
        model=ProduktImage
admin.site.register(ProduktImage, ProduktImageAdmin)
