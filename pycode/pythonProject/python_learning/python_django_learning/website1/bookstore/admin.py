from django.contrib import admin
from . import models
# Register your models here.


class BookManager(admin.ModelAdmin):
    list_display = ['title', 'pub', 'price']
    list_display_links = ['pub']
    list_filter = ['title', 'pub']
    search_fields = ['title', 'price']
    list_editable = ['price']


admin.site.register(models.Book, BookManager)
