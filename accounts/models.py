from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(default=1)
    room_no = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.roll_no})"
    