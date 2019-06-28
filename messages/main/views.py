from django.contrib.auth.views import LoginView, logout_then_login
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from main.forms import UserRegForm, MessageForm, CustomAuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class MSGLoginView(LoginView):
    template_name = 'main/login.html'
    authentication_form = CustomAuthenticationForm
    
def logoutnlogin(request):
    return logout_then_login(request)

class UserRegView(CreateView):
    template_name = 'main/register.html'
    form_class = UserRegForm
    success_url = reverse_lazy('register_done')

class RegDoneView(TemplateView):
    template_name = 'main/register_done.html'
    success_url = reverse_lazy('index')

class MessageView(LoginRequiredMixin, CreateView):
    template_name = 'main/index.html'
    form_class = MessageForm
    success_url = reverse_lazy('message_done')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uid = self.request.user.id
        user = User.objects.get(pk=uid)
        msgs = user.message_set.all()[:5]
        context['msgs'] = msgs
        return context

    def form_valid(self, form):
        """Add to the form data about the user who sent the message """
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class MessageDoneView(LoginRequiredMixin, TemplateView):
    template_name = 'main/message_done.html'
