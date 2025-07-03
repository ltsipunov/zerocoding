from django.contrib.auth import login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView, CreateView

from .models import User
from .forms import CustomUserCreationForm

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self):
        users = User.objects.all().order_by('-id')
        return {'records': users,
                   'title': 'Приложение Users',
                   'header': 'Список пользователей',
                   'empty': 'Список пользователей пуст'}

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    login_url = reverse_lazy('login')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save()
        login(self.request, self.object)
        return HttpResponseRedirect(self.get_success_url())

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))