from django.contrib.auth.views import LoginView, logout_then_login
from django.views.generic.edit import CreateView
from main.forms import UserRegForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required 

@login_required
def index(request):
    return render(request, 'main/index.html')

class MSGLoginView(LoginView):
    template_name='main/login.html'

def logoutnlogin(request):
    return logout_then_login(request)

class UserRegView(CreateView):
        template_name = 'main/register.html'
        form_class = UserRegForm
