from django.contrib import admin

# Register your models here.

from .models import Kniha

class KnihaAdmin(admin.ModelAdmin):
    list_display = ["jmeno", "autor", "rok"]

admin.site.register(Kniha, KnihaAdmin)

