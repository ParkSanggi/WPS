from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(SubUser)


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'is_staff', 'is_superuser', 'auth_token']
    list_display_links = ['username']
    list_editable = ['is_staff', 'is_superuser', ]


admin.site.register(User, UserAdmin)


class LikeDisLikeMaredAdmin(admin.ModelAdmin):
    list_display_links = ['id', 'movie', ]
    list_editable = ['like_or_dislike', 'marked', ]
    list_display = ['id', 'movie', 'like_or_dislike',
                    'marked', 'created', 'updated', ]


admin.site.register(LikeDisLikeMarked, LikeDisLikeMaredAdmin)
