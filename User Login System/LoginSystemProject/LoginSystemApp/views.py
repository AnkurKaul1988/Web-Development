from django.shortcuts import render
from LoginSystemApp.forms import UserForm,ProfileForm
from django.contrib.auth.models import User

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):

    return render(request,'LoginSystemApp/index.html')

def register(request):

    registered = False
    user_form = UserForm()
    profile_form = ProfileForm()

    if request.method  == 'POST':

        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)

            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
            
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:

            print(user_form.errors,profile_form.errors)
    else:
       
        user_form = UserForm()
        profile_form = ProfileForm()
       
    return render(request,'LoginSystemApp/register-form.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})



def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:

            if user.is_active:

                login(request,user)

                return HttpResponseRedirect(reverse('LoginSystemApp:index'))
        
            else:

                return HttpResponse('Account not exists')
        else:

            return HttpResponse('User not found')
    
    return render(request,'LoginSystemApp/login-form.html',{})
 
@login_required
def user_logout(request):

    logout(request)

    return HttpResponseRedirect(reverse('LoginSystemApp:index'))