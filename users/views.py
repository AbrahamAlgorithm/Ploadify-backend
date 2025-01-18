from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view


@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not email or not password:
        return JsonResponse({'error': 'All fields are required.'}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'Username already exists.'}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)
    return JsonResponse({'message': 'User registered successfully.'})

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'message': 'Login successful.'})
    else:
        return JsonResponse({'error': 'Invalid credentials.'}, status=400)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful.'})
