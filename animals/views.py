# animals/views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.views import View
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from .forms import AnimalForm
from .models import Animal
from django.shortcuts import render
from django.utils.translation import activate


def animal_list(request):
    animals = Animal.objects.filter(is_available=True)
    return render(request, 'animals/animal_list.html', {'animals': animals})

def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # После успешного добавления, перенаправление на страницу со всеми животными
            return redirect('animal_list')
    else:
        form = AnimalForm()

    return render(request, 'add_animal.html', {'form': form})


def home(request):
    return render(request, 'animals/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class ProfileView(View):
    def get(self, request):
        return render(request, 'animals/profile.html')

def logout_view(request):
    logout(request)
    return redirect('home')
def home(request):
    return render(request, 'animals/home.html')

def profile(request):
    return render(request, 'animals/profile.html')

logout_view = LogoutView.as_view(next_page='home')

class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        next_url = self.request.GET.get('next', None)
        if next_url:
            return redirect(next_url)
        else:
            return response


def custom_register(request):
    # Реализуйте представление для страницы регистрации
    return render(request, 'animals/register.html')
class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user_profile.html'

