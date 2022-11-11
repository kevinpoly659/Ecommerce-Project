from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    if 'username' in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                request.session['username'] = username
                messages.info(request, 'Logged in Successfully')
                currentuser = request.user
                return render(request, 'index.html', {'currentuser':currentuser})
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('login')
        else:  
            return render(request, 'profile/page-login-register.html')    