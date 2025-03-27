from django.urls import path
from accounts.views import signup_view, login_view, home_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('home/', home_view, name="home"),
    path('login/', login_view, name="login"),
]