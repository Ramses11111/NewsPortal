from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_subscribers', )


admin.site.register(Category, CategoryAdmin, )