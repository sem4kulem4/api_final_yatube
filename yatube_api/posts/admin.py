from django.contrib import admin

from .models import Comment, Group, Follow, Post


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Group)
admin.site.register(Follow)
