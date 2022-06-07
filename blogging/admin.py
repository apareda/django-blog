from django.contrib import admin
from blogging.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


class Categoryline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        Categoryline,
    ]


# and a new admin registration
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
