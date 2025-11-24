

# Register your models here.
from django.contrib import admin
from .models import Activity, Punishment

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('student', 'title', 'date')

@admin.register(Punishment)
class PunishmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'reason', 'date_given', 'resolved')
    list_filter = ('resolved',)
