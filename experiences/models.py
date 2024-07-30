from django.db import models
from users.models import User
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ini = models.DateTimeField()
    date_end = models.DateTimeField(null=True)
    company = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = "experiences"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} | {self.company}"
