

# Create your models here.

from django.db import models
from accounts.models import Student

class FeeRecord(models.Model):
    STATUS_CHOICES = (
        ('PAID', 'Paid'),
        ('PENDING', 'Pending'),
        ('OVERDUE', 'Overdue'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fee_records')
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    paid_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-due_date']

    def __str__(self):
        return f"{self.student} - {self.description} - {self.status}"
