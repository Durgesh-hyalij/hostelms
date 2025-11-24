

# Create your models here.

from django.db import models
from accounts.models import Student

class AttendanceRecord(models.Model):
    STATUS_CHOICES = (
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    remarks = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('student', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.student} - {self.date} - {self.get_status_display()}"
