from django.db import models
from django.conf import settings


class AdModel(models.Model):
    title = models.CharField(max_length=1024)
    body = models.CharField(max_length=16384)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)