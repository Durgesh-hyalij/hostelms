

# Register your models here.

from django.contrib import admin
from .models import AttendanceRecord

@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('student__roll_no', 'student__user__username')
