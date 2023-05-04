from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth import authenticate, login
from .forms import SignupForm
from .utlils import _send_mail_to_users
import uuid
from .models import User
from django.http import HttpResponseRedirect
# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            
            user = form.save(commit=False)
            user.is_active = False
            email = user.email
            token = str(uuid.uuid4())
            user.email_token = token
            _send_mail_to_users(email, token)
            user.save()
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, token):
    user = User.objects.get(email_token=token)
    if user:
        user.is_active = True
        user.save()
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/signup/')
        


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        # if form.is_valid():
        email = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'profile.html')
            
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

