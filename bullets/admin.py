from django.contrib import admin
from .models import Board, Comment

class BoardAdmin(admin.ModelAdmin):
    search_fields = ['title']
    search_fields = ['content']

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['content']

admin.site.register(Board, BoardAdmin)
admin.site.register(Comment, CommentAdmin)