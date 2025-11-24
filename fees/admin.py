
# Register your models here.
from django.contrib import admin
from .models import FeeRecord

@admin.register(FeeRecord)
class FeeRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'description', 'amount', 'due_date', 'status')
    list_filter = ('status',)
    search_fields = ('student__roll_no', 'student__user__username')
