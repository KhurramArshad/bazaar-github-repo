from django.contrib import admin
from .models import Category, Cat_items, Comments
# Register your models here.
admin.site.register(Category)


class Cat_itemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'pid', 'discounted_price', 'category', 'status', ]
    list_filter = ['name', 'pid', 'category', 'status', ]
    date_hierarchy = 'publish'
    ordering = ['status', 'publish', ]
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Cat_items, Cat_itemsAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['item', 'user', 'body', 'created', 'active', ]
admin.site.register(Comments, CommentsAdmin)