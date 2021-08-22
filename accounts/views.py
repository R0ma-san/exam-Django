from django import views
from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import redirect, render, reverse
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm

class LoginView(View):
    
    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {'form':form}
        return render(request, 'accounts/login.html', context)

    def post(slf, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('my_posts'))
        context = {'form':form}
        return render(request, 'accounts/login.html', context)

class RegistrationView(View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {'form':form}
        return render(request, 'accounts/register.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect(reverse('new_post'))
        context = {'form':form}
        return render(request, 'accounts/register.html', context)

