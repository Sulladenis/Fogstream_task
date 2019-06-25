from django.urls import path

from .views import UserRegView, index, MSGLoginView
from .views import logoutnlogin
urlpatterns = [
        path('', index, name='index'),
        path('login/', MSGLoginView.as_view(), name='login'),
        path('logout/', logoutnlogin, name='logout'),
        path('register/', UserRegView.as_view(), name='register'),
        ]
