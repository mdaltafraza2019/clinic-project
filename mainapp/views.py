from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from mainapp.forms import Registerform
from mainapp.forms import *
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(r):
    return render(r,'base.html')
def register(r):
     form=Registerform(r.POST or None)
     if r.method=='POST':
          if form.is_valid():
               form.save()
               messages.success(r,'you are succesfully registered!!!')
               return redirect(loginfun)
     return render(r,'register.html',{'form':form})
def loginfun(r):
    form=AuthenticationForm(r.POST or None)
    if r.method=='POST':
        
          username=r.POST.get('username')
          password=r.POST.get('password')
          user=authenticate(username=username,password=password)
          if user is not None:
               if user.is_superuser:
                    return HttpResponseRedirect('/admin/')
               login(r,user)
               
               return redirect(home)
          else:
               messages.error(r,'invalid  username or password !!!') 
               return redirect(login)
    return render (r,'login.html',{'form':form})

def logoutfun(r):
     logout(r)
     return redirect(home)


