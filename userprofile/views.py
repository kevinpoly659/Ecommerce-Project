from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . models import Account,Address, Profile,Guest
from .helper import MessageHandler
import random
from orders.models import Order,OrderProduct

# Create your views here.
def user_login(request):
    if 'username' in request.session:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request,user)
                request.session['username'] = username
                messages.info(request, 'Logged In Successfully')
                currentuser = request.user
                return render(request, 'index.html', {'currentuser' : currentuser})
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('home')
        else:
            return render(request, 'profile/user-login.html')
        

def user_signup(request):
    print("aaaaaaaa")
    if request.method =='POST':      
        print("bbbbbb")  
        username = request.POST['username']   
        first_name = request.POST['first_name']                
        last_name = request.POST['last_name']                
        email = request.POST['email']                
        phone_number = request.POST['phone_number']                
        password1 = request.POST['password1']                             
        password2 = request.POST['password2']  
        if password1 ==password2:
            if username=="":
                messages.error(request,"username is empty")
                return render(request,'profile/user-signup.html')              
            
            elif len(username)<2:
                messages.error(request,"username is too short")
                return render(request,'profile/user-signup.html')  
            
            elif not username.isidentifier():
                messages.error(request,"username start must with alphabets")
                return render(request,'profile/user-signup.html')                     
            
            elif Account.objects.filter(username = username):
                messages.error(request,"username exits")
                return render(request,'profile/user-signup.html')
            
            elif email=="":
                messages.error(request,"email field is empty")
                return render(request,'profile/user-signup.html')
            
            elif len(email)<2:
                messages.error(request,"email is too short")
                return render(request,'profile/user-signup.html')

            elif Account.objects.filter(email=email):
                messages.error(request,"email already exist try another")
                return render(request,'profile/user-signup.html')
            
            user1 =Account.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1,phone_number=phone_number)
            user1.save()
        messages.success(request,"Registered Successfully")
    return render(request,'profile/user-signup.html') 
        

@login_required
def user_logout(request):
    request.session.flush()
    messages.success(request, "Logged Out Successfully")
    return redirect('home')
        
def user_otp_login(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        profile = Account.objects.filter(phone_number = phone_number)
        if not profile.exists():
            messages.info(request, 'Phone Number Not Registered With')
            return redirect('userlogin')
        else:
            profile1 = Account.objects.get(phone_number=phone_number)
            profile1.otp = random.randint(1000,9999)
            profile1.save()
            messagehandler = MessageHandler(phone_number, profile1.otp)
            messagehandler.send_otp_via_message()

            messages.info(request, 'Otp Sent Successfully')

            context = {'phone_number':profile1.phone_number}            
            
            return render(request,'profile/user-otp-verify.html',context)
    return render(request,'profile/user-otp.html')


def otp(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        try:
            profile = Account.objects.get(otp=otp)
        except:
            messages.info(request,"Wrong OTP")
            return redirect('otplogin')
        if profile.otp == otp:
            login(request, profile)
            messages.info(request, 'Logged in Successfully')
            currentuser = request.user
            return render(request, 'index.html', {'currentuser':currentuser})
        
    return render(request, 'profile/user-otp.html')
    


def user_account(request):
    try:    
        currentuser = request.user
        account = Account.objects.get(username=request.user.username)
        
        orders = Order.objects.filter(user = currentuser) 
        try:
            address = Address.objects.filter(user = currentuser)
        except:
            return redirect('addaddress')
    except:
        account = Guest.objects.get(name='guest')
        orders = Order.objects.filter(guest =(Guest.objects.get(name='guest'))) 
        try:
            address = Address.objects.filter(guest =(Guest.objects.get(name='guest')))
        except:
            return redirect('addaddress')
        
        
    return render(request, 'profile/user-account.html',{'current':currentuser, 'address':address, 'orders':orders,'account':account})


def user_view_order(request, id):
    
    orders = Order.objects.get(id=id)
    OrderProducts = OrderProduct.objects.filter(order = orders)
    
    return render(request, 'profile/user-order-view.html', {'orders':orders, 'order_details':OrderProducts})


def user_return_order(request,id):
    orders = Order.objects.get(id=id)
    if request.method == 'POST':
        reason = request.POST['reason']
        orders.reasonreturn = reason
    orders.status = 'Returned'
    orders.save()
    return redirect('vieworder',id)

def user_cancel_order(request, id):
    orders = Order.objects.get(id=id)
    if request.method == 'POST':
        reason = request.POST['reason']
        orders.reasoncancel = reason
    orders.status = 'Cancelled'
    orders.save()
    return redirect('vieworder', id)

def user_add_address(request):
    try:
        currentuser = request.user
        if request.method == 'POST':
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            phone_number = request.POST['phone_number']
            email = request.POST['email']
            address = request.POST['Address']
            town = request.POST['Town']
            state = request.POST['State']
            pincode = request.POST['Pin']
            
            
            user1 = Address.objects.create(user=currentuser)
            user1.firstname=firstname
            user1.lastname=lastname
            user1.phone_number=phone_number
            user1.Email_Address=email
            user1.Addressfield=address
            user1.Town=town
            user1.state=state
            user1.pincode=pincode
            user1.save()
            return redirect('account')
    except:
        if request.method == 'POST':
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            phone_number = request.POST['phone_number']
            email = request.POST['email']
            address = request.POST['Address']
            town = request.POST['Town']
            state = request.POST['State']
            pincode = request.POST['Pin']
            
            
            user1 = Address.objects.create(guest=(Guest.objects.get(name='guest')))
            user1.firstname=firstname
            user1.lastname=lastname
            user1.phone_number=phone_number
            user1.Email_Address=email
            user1.Addressfield=address
            user1.Town=town
            user1.state=state
            user1.pincode=pincode
            user1.save()
            return redirect('viewcart',0)
    return render(request, 'profile/user-add-address.html')

def delete_address(request,id):
    add = Address.objects.get(id=id)
    add.delete()
    return redirect('account')

def user_edit_account(request):
    account = Account.objects.get(username=request.user.username)
    if request.method=='POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email = request.POST['email']        
        phone_number = request.POST['phone_number']     
        
        try:
            password = request.POST['password']         
            passwordn = request.POST['npassword'] 
            passwordc = request.POST['cpassword'] 
            if account.check_password(password):
                if passwordn == passwordc:
                    account.set_password(passwordn)  
                    if account.first_name != first_name:
                        account.first_name = first_name
                    if account.last_name != last_name:
                        account.last_name = last_name
                    if account.email != email:
                        account.email = email
                    if account.phone_number != phone_number:
                        account.phone_number = phone_number 
                    account.save()
                else:
                    messages.info(request,"Passwords not matching")
            else:
                messages.info(request,"Incorrect Password")
        except:
            if account.first_name != first_name:
                account.first_name = first_name
            if account.last_name != last_name:
                account.last_name = last_name
            if account.email != email:
                account.email = email
            if account.phone_number != phone_number:
                account.phone_number = phone_number 
            account.save()
        
    return redirect('userlogin')
