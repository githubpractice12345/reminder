from django.db import models

# Create your models here.
class Reminder(models.Model):
    class ReminderMetod(models.TextChoices):
        SMS = 'SMS', 'Text Message'
        EMAIL = 'EMAIL', 'Email Message'
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_method = models.CharField(max_length=10,choices=ReminderMetod.choices)

    def __str__(self):
        return f"{self.reminder_method} - {self.date} {self.time}"