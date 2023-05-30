from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class ParsUserManager(BaseUserManager):
    def create(self, email, password=None):
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None):
        user = self.create(email, password)
        user.is_admin=True
        user.save()
        return user



        


class ParsUserModel(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = ParsUserManager()

    USERNAME_FIELD="email"

    
    @property
    def is_authenticated(self):
        return True
    
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_superuser(self):
        return self.is_admin
    
    @property
    def is_staff(self):
        return self.is_active
