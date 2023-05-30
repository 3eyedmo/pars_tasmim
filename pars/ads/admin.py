from django.contrib import admin
from ads.models import AdModel


@admin.register(AdModel)
class AdModelAdmin(admin.ModelAdmin):
    list_display = (
        "id", "title", "body", "author"
    )