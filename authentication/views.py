from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from . models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import JsonResponse



def create_account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if confirm_password != password:
            messages.error(request, "Password mismatch")
        else:
            user = User(username=username, email=email)
            user.set_password(password)  
            user.save()
            messages.success(request, "Account created successfully")

        return HttpResponse("Success")

    return render(request, 'user_auth/sign-up.html')  



def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return JsonResponse({'message': 'Login successful', 'redirect_url': reverse('core:index')}, status=200)
        else:
            messages.error(request, "Invalid email or password")
            return JsonResponse({'message': 'Invalid email or password'}, status=401)
    return render(request, 'user_auth/sign-in.html')



def logout_user(request):
    logout(request)
    return redirect(reverse('user_auth:sign-in'))
