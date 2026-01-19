from django.contrib import admin
from django.urls import path
from pm_core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
]