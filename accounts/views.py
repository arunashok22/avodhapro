from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth


# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['Username']
        password=request.POST['Password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,"login.html")



def register(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['Username']
        password1=request.POST['Password1']
        password2=request.POST['Password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user= User.objects.create_user(username=username, password=password1, email=email, first_name=firstname, last_name=lastname)
                user.save()
                print("user created")
                return redirect('login')
        else:
            print("Passwod not matched")
            return redirect('register')

    return render(request, "register.html")



def logout(request):
    auth.logout(request)
    return redirect('/')
