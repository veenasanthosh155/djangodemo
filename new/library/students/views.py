from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        fname = request.POST['x']
        lname = request.POST['y']
        e = request.POST['e']
        ph = request.POST['ph']
        pl = request.POST['pl']

        if (p == cp):
            u = CustomUser.objects.create_user(username=u, password=p, first_name=fname, last_name=lname, email=e, phone=ph, place=pl)
            u.save()
            return redirect('books:home')
        else:
            return HttpResponse("Passwords are not same")
    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('books:home')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,'login.html',)

@login_required
def user_logout(request):
    logout(request)
    return redirect('students:login')
