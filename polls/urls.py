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
  path('questions3/', views.questions3, name='questions3'),
  path('submit3/', views.submit3, name='submit3'),
  path('thank_you3/', views.thank_you3, name='thank_you3'),
  path('questions4/', views.questions4, name='questions4'),
  path('submit4/', views.submit4, name='submit4'),
  path('thank_you4/', views.thank_you4, name='thank_you4'),
  path('questions5/', views.questions5, name='questions5'),
  path('submit5/', views.submit5, name='submit5'),
  path('thank_you5/', views.thank_you5, name='thank_you5'),
  path('questions6/', views.questions6, name='questions6'),
  path('submit6/', views.submit6, name='submit6'),
  path('thank_you6/', views.thank_you6, name='thank_you6'),
  path('SurveryCompleted/', views.SurveryCompleted, name='SurveryCompleted'),
]
