from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Tweet(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  message = models.CharField(max_length=100)
  created_at = models.DateTimeField(default=datetime.now())

  def __str__(self):
    return self.user.username

