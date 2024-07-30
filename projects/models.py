from django.db import models
from users.models import User
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    url = models.URLField(null=True)
    description = models.TextField()

    class Meta:
        db_table = "projects"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} | {self.title}"
