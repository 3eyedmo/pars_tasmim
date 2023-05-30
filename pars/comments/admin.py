from django.contrib import admin
from comments.models import CommentModel


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = (
        "id", "text", "ad", "author"
    )