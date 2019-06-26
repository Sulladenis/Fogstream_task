from django.contrib.auth.views import LoginView, logout_then_login
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from main.forms import UserRegForm, MessageForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class MSGLoginView(LoginView):
    template_name='main/login.html'
    
def logoutnlogin(request):
    return logout_then_login(request)

class UserRegView(CreateView):
    template_name = 'main/register.html'
    form_class = UserRegForm
    success_url = reverse_lazy('register_done')

class RegDoneView(TemplateView):
    template_name = 'main/register_done.html'

class MessageViwe(CreateView, LoginRequiredMixin):
    template_name = 'main/index.html'
    form_class = MessageForm
    success_url = reverse_lazy('message_done')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MessageDoneView(TemplateView, LoginRequiredMixin):
    template_name = 'main/message_done.html'

    
    

