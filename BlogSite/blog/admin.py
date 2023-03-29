from django.contrib import admin
from . models import *
# Register your models here.

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Categories,CategoryModelAdmin)

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','category','slug','created')
admin.site.register(Post,PostModelAdmin)

class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ('post','author_name','comments', 'created')
admin.site.register(Comments,CommentsModelAdmin)