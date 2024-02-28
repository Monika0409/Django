from django.contrib import admin

# Register your models here.

from .models import Countrys,Citys, Subject1s, Markss

admin.site.register(Citys)
admin.site.register(Countrys)
admin.site.register(Subject1s)
admin.site.register(Markss)



