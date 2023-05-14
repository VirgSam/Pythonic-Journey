from django.contrib import admin
from . models import Tag, Author, Post, Comment

class TagAdmin(admin.ModelAdmin):
    pass
class AuthorAdmin(admin.ModelAdmin):
    pass
class PostAdmin(admin.ModelAdmin):
    list_filter = ("author","tags","date" )
    list_display = ("title","date","author")
    prepopulated_fields= {"slug":("title",)}

class CommentAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

