from django.db import models
from django.contrib.auth.models import AbstractUser
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class User(AbstractUser):
    email = models.EmailField("email", unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]

    modified = models.DateTimeField(auto_now=True)
    photo = models.ImageField(null=True, upload_to="users")
    description = models.TextField()
    phone = models.CharField(null=True, max_length=12)
    city = models.CharField(null=True, max_length=20)
    country = models.CharField(null=True, max_length=20)
    is_recruiter = models.BooleanField(default=False)

    class Meta:
        db_table = "users"
