from django.core import serializers
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from shop.models import Category
import json

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from shop.forms import UserRegisterForm, UserLoginForm

class UserRegisterFormView(View):
    form_class = UserRegisterForm
    template_name = 'shop/registration_form.html'

    #display a form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #clean normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return User
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form})

class UserLoginFormView(View):
    form_class = UserLoginForm
    template_name = 'shop/login_form.html'

    # display a form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(None)
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return redirect('index')
            else:
                # An inactive account was used - no logging in!
                return render(request, self.template_name, {'form': form, 'message' : 'Your account is disabled'})
        else:
            # Bad login details were provided. So we can't log the user in.
            return render(request, self.template_name, {'form': form, 'message': 'Invalid login details supplied.'})

            # The request is not a HTTP POST, so display the login form.
            # This scenario would most likely be a HTTP GET.

def UserLogout(request):
    logout(request)
    return redirect('login')