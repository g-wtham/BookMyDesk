from django.urls import path
from accounts.views import test_view

urlpatterns = [
    path('test/', test_view)
]