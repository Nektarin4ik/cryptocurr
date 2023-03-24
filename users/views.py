from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView

from .forms import UserLoginForm, UserProfileForm, UserRegistrationForm


class UserRegistrationView(CreateView):

    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('cryptopage:index')


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


class LoginProfileView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('cryptopage:index')


class logout(View):

    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('cryptopage:index'))
