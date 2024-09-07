from django.contrib import admin
from .models import  Author,Post,Tag,Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','date')
    list_filter = ('author','date','tags',)
    #search_fields = ('title','content')
    prepopulated_fields={'slug':('title',)}
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name','post')
    list_filter = ('user_name','post')
    search_fields = ('user_name','post')
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
