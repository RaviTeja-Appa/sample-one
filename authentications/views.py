from django.contrib.auth import logout
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import User

from django.shortcuts import render, redirect
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            date_of_birth = form.cleaned_data['date_of_birth']

            user = User.objects.create_user(
                email=email,
                username=username,
                password=password,
                date_of_birth=date_of_birth
            )

            # Authenticate and login the user after registration
            # user = authenticate(request, username=username, password=password)

            login(request, user)

            request.session['registration_success'] = True

            return redirect('home')  # Redirect to home after login

    else:
        form = RegistrationForm()

    return render(request, 'index.html', {'form': form, 'domain': 'signup', 'error_message': form.errors})


def user_login(request):
    error_message = None  # Initialize error message

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the home page after login
            # Assuming 'home' is the URL name for home.html
            return redirect('home')
        else:
            error_message = "Invalid username or password"

    # Render the login overlay with the error message if exists
    return render(request, 'index.html', {'login_error_message': error_message, 'domain': 'login'})


@login_required
def user_logout(request):
    logout(request)
    return redirect('register')


@login_required
def home(request):

    return render(request, 'home.html')

    registration_success = request.session.pop('registration_success', False)
    context = {
        'registration_success': registration_success} if registration_success else {}

    return render(request, 'home.html', context)
