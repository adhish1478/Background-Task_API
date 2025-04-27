from . import views
from django.urls import path

urlpatterns=[
    #path('trigger-task', TriggerTask.as_view(), name='trigger_task'),
    path('trigger', views.trigger_background_task, name='trigger_background_task')
]