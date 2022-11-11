from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def admin_login(request):
    if 'username' in request.session:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_superuser:
                login(request,user)
                request.session['username'] = username
                messages.info(request, 'Logged in Successfully')
                currentuser = request.user
                return render(request, 'ad/index-admin.html', {'currentuser':currentuser})
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('login')
        else:  
            return render(request, 'ad/page-account-login.html')
@login_required
def dashboard(request):
    return render(request, 'ad\index-admin.html')


@login_required
def admin_logout(request):
    request.session.flush()
    messages.success(request, "Logged Out Successfully")
    return redirect('login')