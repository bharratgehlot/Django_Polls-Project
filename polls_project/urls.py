from django.contrib import admin
from django.urls import path, include
from polls.views import home_redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include(('polls.urls', 'polls'), namespace='polls')),
    path("", home_redirect, name="home"),
]
