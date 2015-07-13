from django.contrib import admin
from .models import Person, Otro

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'initials')

admin.site.register(Person, PersonAdmin)

admin.site.register(Otro)