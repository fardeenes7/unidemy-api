from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from uuid import uuid4

# Create your models here.
class CustomUserModelManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using = self._db)

        return user
    
    def create_superuser(self, username, email, password=None):
        user = self.create_user(email, username, password)
        user.save()
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)

        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(max_length=100,primary_key=True, editable=False, blank=True, default=uuid4)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    active = models.BooleanField(default=True)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserModelManager()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'User'