from django.contrib import admin

# Register your models here.

from .models import Name, Contract, Group


admin.site.register(Name)
admin.site.register(Contract)
admin.site.register(Group)
