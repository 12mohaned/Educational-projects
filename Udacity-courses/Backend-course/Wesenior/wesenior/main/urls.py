"""wesenior URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import url, include
from django.contrib import admin
from . import views
app_name = "main"
urlpatterns = [
    url("Home",views.homepage,name = "homepage"),
    url("signup",views.signup,name = "signup"),
    url("ourstory",views.OurStory,name = "aboutus"),
    url("logout",views.logout_request,name = "logout"),
    url("login",views.login_request,name = "login"),
    #url("<single_slug>",views.single_slug,name = "single_slug"),
    #url("courses",views.courses,name = "courses"),
    url("become_a_tutor",views.BecomeaTutor,name = "BecomeaTutor"),
    url("home",views.homepage2,name = "homepage2")
]
