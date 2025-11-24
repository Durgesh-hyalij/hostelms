

# Create your models here.
from django.db import models
from accounts.models import Student

class Room(models.Model):
    number = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField(default=3)
    floor = models.IntegerField(default=1)

    def __str__(self):
        return f"Room {self.number} (Floor {self.floor})"

class RoomAllocation(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='allocation')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='allocations')
    join_date = models.DateField()
    leave_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} -> {self.room}"
