from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
  path('', views.home_redirect, name='home_redirect'),
  path('questions/', views.questions, name='questions'),
  path('submit/',views.submit, name="submit"),
  path('thank_you/', views.thank_you, name='thank_you'),
  path('questions2/', views.questions2, name='questions2'),
  path('submit2/', views.submit2, name='submit2'),
  path('thank_you2/', views.thank_you2, name='thank_you2'),
]
