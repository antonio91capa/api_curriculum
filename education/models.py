from django.db import models
from users.models import User


# Create your models here.
class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ini = models.DateTimeField()
    date_end = models.DateTimeField(null=True)
    title = models.CharField(max_length=200)

    class Meta:
        db_table = "educations"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} | {self.title}"
