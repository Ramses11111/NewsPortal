from django.contrib import admin
from .models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('authorUser', 'ratingAuthor')
    list_filter = ('ratingAuthor',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_subscribers')


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'category_type', 'dateCreation', 'preview', 'rating')
    list_filter = ('author', 'category_type', 'dateCreation', 'rating')
    search_fields = ('author', 'category_type', 'dateCreation', 'rating')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('dateCreation', 'rating')
    list_filter = ('dateCreation', 'rating')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.unregister(PostCategory)
