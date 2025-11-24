

# Register your models here.

from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll_no', 'year', 'room_no')
    search_fields = ('user__username', 'roll_no', 'room_no')
