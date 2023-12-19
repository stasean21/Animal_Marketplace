from django.urls import path
from django.contrib.auth import views as auth_views
from .views import animal_list, add_animal, home, register
from .views import ProfileView, logout_view, CustomLoginView
from .views import UserProfileView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),  # Добавлен маршрут для регистрации
    path('login/', CustomLoginView.as_view(), name='login'),
    path('animal_list/', animal_list, name='animal_list'),
    path('animal_list/add/', add_animal, name='add_animal'),
    path('', home, name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', logout_view, name='logout'),
    path('accounts/profile/', UserProfileView.as_view(), name='user_profile'),
    path('accounts/logout/', LogoutView.as_view(next_page='home'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)