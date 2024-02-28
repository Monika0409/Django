from django.contrib import admin

from .models import bookss


class booksAdmin(admin.ModelAdmin):


    list_display  = ['book_name','subject']

admin.site.register(bookss,booksAdmin)

# Register your models here.
