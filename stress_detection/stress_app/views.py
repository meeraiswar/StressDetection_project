# stress_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm, StressDataForm
from .models import StressData

def home(request):
    return render(request, 'stress_app/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)  # Hash the password
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'stress_app/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('data_input')
    else:
        form = AuthenticationForm()
    return render(request, 'stress_app/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def data_input(request):
    if request.method == 'POST':
        form = StressDataForm(request.POST)
        if form.is_valid():
            stress_data = form.save(commit=False)
            stress_data.user = request.user  # Link data to logged-in user
            stress_data.calculate_stress()  # Calculate stress
            return redirect('result')
    else:
        form = StressDataForm()
    return render(request, 'stress_app/data_input.html', {'form': form})
# stress_app/views.py
def result(request):
    user_data = StressData.objects.filter(user=request.user).last()  # Get the last stress data
    return render(request, 'stress_app/result.html', {'user_data': user_data})

