from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from account.models import User

# Create your views here.

class LoginView(View):
    template_name = 'account/login.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('username')
        password =self. request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                if user.reset_password:
                    return redirect('passwordform',user.username)
            except User.DoesNotExist:
                messages.warning(request,'info provided does not exist')
                return redirect('login')
    
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,'Incorrect username or password')
            return redirect('login')

def logoutuser(request):
    logout(request)
    return redirect('login')

class RegisterView(View):
    template_name = 'account/register.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):
        pass

def comingSoon(request):
    return render(request, 'account/coming_soon.html')