from django.contrib import admin

from .models import Board, Image_Posting, Like, Comment, Following

from .models import Board, Image_Posting, Like, Comment, Following, Save_Post

admin.site.register(Board)
admin.site.register(Image_Posting)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Following)
admin.site.register(Save_Post)
