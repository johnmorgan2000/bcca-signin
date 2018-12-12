from django.shortcuts import render, redirect
from django.views import View
import datetime
from . import models
from . import forms

# Create your views here.


class GetHome(View):
    def get(self, request):
        return render(request, 'index.html',
                      {'students': models.Student.signins_for_today()})


class SignInUser(View):
    def get(self, request):
        return render(request, 'signin.html', {
            'signin_form': forms.SignInForm(),
        })

    def post(self, request):
        form = forms.SignInForm(data=request.POST)

        if form.is_valid():
            models.Student.sign_in(form.cleaned_data['name'])
            return redirect("home")
        else:
            return render(request, 'signin.html', {'signin_form': form})


class SignInSince(View):
    def get(self, request):
        return render(request, 'signins_since.html',
                      {'since_form': forms.SignInSince()})

    def post(self, request):
        form = forms.SignInSince(data=request.POST)

        if form.is_valid():
            date = form.cleaned_data['date']
            sign_ins = models.Student.get_signins_since(date)

            return render(request, 'signins_since.html', {
                'since_form': forms.SignInSince(),
                'sign_ins': sign_ins,
            })
        else:
            return render(request, 'signins_since.html', {'since_form': form})
