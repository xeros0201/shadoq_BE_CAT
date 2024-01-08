from django.urls import path
from user import views




urlpatterns = [
    path('',views.GET),
    path('/create',views.POST),
]