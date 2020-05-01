from django.shortcuts import render,redirect
from django.templatetags.static import static
from django.contrib.auth import authenticate,login,logout
from .forms import EmpSignupForm,EmpLoginForm,UserSignupForm,UserLoginForm
import django.urls
from django.contrib.auth.models import User

# Create your views here.
def IndexView(request):
    return render(request,'index.html')

    
def EmpsignupView(request):
    if request.method == 'POST':
        # print(request.POST)
        form1 = EmpSignupForm(request.POST)
        if form1.is_valid():
            print("form is valid")
            form1.save()    
            return redirect('/') #render(request,'empsignup.html',context={'form1':signup_form})
        else:
            print(form1.errors)
    signup_form = EmpSignupForm()
    return render(request,'empsignup.html',context={'form1':signup_form})

def EmploginView(request):
    if request.user.is_staff:
        return redirect("/emp")
    if request.method == 'POST':
        # print(request.POST['password'])
        user = authenticate(username=request.POST['username'],password=request.POST['password'],is_staff=1)
        # print(user)
        if user is not None:
            print("authenticated...redirecting user")
            login(request,user)
            return redirect('/emp')
            # return redirect(urls.reverse('index'))
        print(user)
        pass
    form1 = EmpLoginForm()
    return render(request,'emp_login.html',context={'form1':form1})

def EmplogoutView(request):
    if request.user.is_authenticated:
        # print(request.user)
        logout(request)
        # print(request.user)
        return render(request,'emp_logout.html',context={'message':"Employee Logged Out"})
    else:
        return render(request,'emp_logout.html',context={'message':"No active session present"})

def EmpchgpasswdView(request):
    if request.method== 'POST':
        p1 = request.POST['p1']
        p2 = request.POST['p2']
        if p1 == p2:
            u = User.objects.get(username=request.user.username)
            if u:
                u.set_password(p1)
                message = "Password changed successfully"
                alert_class = "success"
        else:
            message = "Password didnt match"
            alert_class = "warning"
    else:
        message = ""
        alert_class = "primary"
    return render(request,'emp_password_reset.html',context={'message':message,"alert_class":alert_class})
    

def UserloginView(request):
    if request.method == 'POST':
        # print(request.POST['password'])
        user = authenticate(username=request.POST['username'],password=request.POST['password'],is_staff=0)
        # print(user)
        if user is not None:
            print("authenticated...redirecting user")
            login(request,user)
            return redirect('/index')
            # return redirect(urls.reverse('index'))
        print(user)
        pass
    form1 = UserLoginForm()
    return render(request,'user_login.html',context={'form1':form1})

def UsersignupView(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form1 = UserSignupForm()
    return render(request,'user_signup.html',context={"form1":form1})

def UserslogoutView(request):
    if request.user.is_authenticated:
        # print(request.user)
        logout(request)
        # print(request.user)
        return render(request,'user_logout.html',context={'message':"User Logged Out"})
    else:
        return render(request,'user_logout.html',context={'message':"No active session present"})