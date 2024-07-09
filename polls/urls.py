
from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
  path('questions/', views.questions, name='questions'),
  path('submit',views.submit, name="submit"),
  path('thank_you', views.thank_you, name='thank_you'),
]
