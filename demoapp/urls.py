from django.urls import path
from demoapp.views import HomePage

urlpatterns = [
    path('', HomePage.as_view()),
]