from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def index(request):
    return render(request, 'patient/patient-predict.html')


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        else:
            return redirect('index')
    else:
        form = AuthenticationForm()
        return render(request, 'login', {'form': form})


def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('account:Login')
