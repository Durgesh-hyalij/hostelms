

# Create your models here.
from django.db import models
from accounts.models import Student

class Activity(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='activities')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.student}"

class Punishment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='punishments')
    reason = models.CharField(max_length=255)
    date_given = models.DateField()
    action_taken = models.TextField()
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.reason}"
