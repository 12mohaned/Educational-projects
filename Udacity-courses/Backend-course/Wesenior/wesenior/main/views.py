# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutor, Majors, Courses
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm, TutorForm
def Tutors_url(request):
    return render(request, template_name='main/tutors.html',context = {"Tutors":  Tutor.objects.all})
def Courses_url(request):
    return render(request, template_name='main/courses.html',context = {"Courses" :Courses.objects.all,"request":request})
def single_slug(request, single_slug):
    Tutors = [m.Tutors_slug  for m in Majors.objects.all()]
    if single_slug in Tutors:
        return HttpResponse("Hello")
    else :
        return HttpResponse("Bye")
    courses = [c.Courses_slug for c in Majors.objects.all()]
    if single_slug in courses:
        return HttpResponse("Bello")
    else :
        return HttpResponse("Bye")
def homepage(request):
        return render(request = request,template_name = 'main/home.html',
                  context ={"majors":Majors.objects.all})
def homepage2(request):
    return render(request = request,template_name = 'main/home2.html',
              context ={"majors":Majors.objects.all})
def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = NewUserForm
    return render(request,"main/signup.html",context = {"form":form})
def OurStory(request):
    return render(request = request, template_name = "main/ourstory.html")
def logout_request(request):
    logout(request)
    return redirect("main:homepage")
def login_request(request):
   if request.method == "POST":
       form = AuthenticationForm(request,data = request.POST)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(username=username, password=password)
           if user is not None :
               login(request, user)
               return redirect('main:homepage')
           else:
               return HttpResponse("Sorry")
       else:
           return ""
   form = AuthenticationForm()
   return render(request,template_name= "main/login.html",context ={"form":form})
#def courses(request):
#    return render(request,template_name ="main/courses.html",context = {"courses":Courses.objects.all,"majors":Majors.objects.all})
#def tutors(request):
#    return render(request,template_name="main/tutors.html",context= {"tutors":tutors.objects.all})
def BecomeaTutor(request):
    if request.method == "POST":
        form = TutorForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    form = TutorForm
    return render(request,"main/become_a_tutor.html",context = {"form":form})
def Tutor(request, Major):
    return render(request,"main/tutors.html",context = {"majors":Majors.objects.all})
