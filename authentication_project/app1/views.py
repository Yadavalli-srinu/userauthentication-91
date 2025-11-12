from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def reg_form(request):
    message=''
    if request.method=="POST":
        username=request.POST.get('user_name')
        useremail=request.POST.get('user_email')
        userp1=request.POST.get('user_password')
        userp2=request.POST.get('user_c_password')

        if userp1!=userp2:
            message='Please Enter Valid Password'
        elif User.objects.filter(email=useremail).exists():
            message='Email Already Exists'
        else:
            user=User.objects.create_user(username=username,email=useremail,password=userp1)
            user.save()
            message='User Creates Successfully'
            return redirect('log101')
    return render(request,'frontend_app1/reg.html',{'message':message})

def log_form(request):
    message=''
    if request.method=='POST':
        username=request.POST.get('user_login_name')
        userpasword=request.POST.get('user_login_password')

        user=authenticate(request,username=username,password=userpasword)

        if user is not None:
            login(request,user)
            message='Login Successfully'
        else:
            message='Invalid Details'
    return render(request,'frontend_app1/log.html',{"message":message})
