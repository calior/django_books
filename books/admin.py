# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from books.models import Publisher, Author, Book
from django.contrib import admin

# Register your models here.

class PublisherAdmin(admin.ModelAdmin):
    pass

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publisher_date')
    list_filter = ('publisher_date','publisher')
    date_hierarchy = 'publisher_date'
    ordering = ('-publisher_date',)
    fields = ('title', 'author', 'publisher', 'publisher_date')
    filter_horizontal = ('author',)
    # filter_vertical = ('author',)
    raw_id_fields = ('publisher',)

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)