from django.contrib import admin
from api.models import Reminder
# Register your models here.
class ReminderAdmin(admin.ModelAdmin):
    list_display = ['id', 'reminder_method', 'date', 'time', 'message']
admin.site.register(Reminder,ReminderAdmin)