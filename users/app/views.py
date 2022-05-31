import http
from django.shortcuts import render
from app.forms import UserForm, UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'app/index.html')


def registration(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

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
            print(profile_form.errors, user_form.errors)
            
            
            # if 'portfolio_site' in request.FILES:
            #     profile.portfolio_site = request.FILES['portfolio_site']
            # else:
            #     print(profile_form.errors, user_form.errors)

            

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'app/registration.html', 
    {'registered':registered, 
    'user_form':user_form,
    'profile_form':profile_form})



def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print("failed login, username: {}, password: {}".format(username, password))
                return HttpResponse('USER NOT ACTIVE!')

    else:
        return render(request, 'app/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("Welcome to special page")
 















