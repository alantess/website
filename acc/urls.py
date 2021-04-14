from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='homepage'),
    path('portfolio/', views.home, name='portfolio')
]
