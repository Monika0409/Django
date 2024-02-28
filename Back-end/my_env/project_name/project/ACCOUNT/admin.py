from django.contrib import admin

from .models import finances


class financeAdmin(admin.ModelAdmin):


    list_display  = ['head_name','title']

admin.site.register(finances,financeAdmin)


# Register your models here.
