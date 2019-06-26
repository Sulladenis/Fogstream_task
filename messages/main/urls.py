from django.urls import path
from django.views.generic.base import TemplateView
from .views import UserRegView, MessageViwe, MSGLoginView, RegDoneView
from .views import logoutnlogin, MessageDoneView
urlpatterns = [
        path('', MessageViwe.as_view(), name='index'),
        path('login/', MSGLoginView.as_view(), name='login'),
        path('logout/', logoutnlogin, name='logout'),
        path('register/', UserRegView.as_view(), name='register'),
        path('register/done/', RegDoneView.as_view(), name ='register_done'),
        path('message/done/', MessageDoneView.as_view(), name ='message_done')
        ]
