from django.urls import path
from api.views import ReminderCreateView

urlpatterns = [
    path('reminder/',ReminderCreateView.as_view(), name='reminder-create')
]
