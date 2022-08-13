from django.contrib import admin
from .models import BookGenres, Books

# Register your models here.
admin.site.register(BookGenres)

@admin.register(Books)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields =  {'slug': ('title',),}