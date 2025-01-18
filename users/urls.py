from django.urls import path
from . import views  # Import your views from the users app

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # Ensure this matches your view name
    path('logout/', views.logout_view, name='logout'),
]
