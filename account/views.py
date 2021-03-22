from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/sign_up.html', {'error': 'Username has already taken'})

            except User.DoesNotExist:
                user = User.objects.create_user(
                                            request.POST['username'], 
                                            password=request.POST['password1'] )
                auth.login(request, user)
                return redirect('home')
        
        else:
            return render(request, 'accounts/sign_up.html', {'error': 'Passowords must match'})
            
    else:
        pass

    return render(request, 'accounts/sign_up.html')


def log_in(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            auth.login(request, user)
            print("hello")
            return redirect('home')
        else:
            return render(request, 'accounts/log_in.html', {'error': 'Username or password is wrong'})
    return render(request, 'accounts/log_in.html')


def log_out(request):
    #log out and redirect to home.html
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    
    return render(request, 'accounts/log_out.html')
