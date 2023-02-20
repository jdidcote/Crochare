from django.contrib.auth.models import User
from django.db import models


class Pattern(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pattern_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.pattern_name
