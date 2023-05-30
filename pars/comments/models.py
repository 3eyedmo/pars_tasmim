from django.db import models
from django.conf import settings
from ads.models import AdModel



class CommentModel(models.Model):
    text = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    ad = models.ForeignKey(AdModel, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.text
    
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
