from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100, null=False)
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=5000, null=False)
    date_and_time = models.DateTimeField()
