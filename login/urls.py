from django.urls import path

from .views import *

app_name = 'login'
urlpatterns = [
	path('',index,name='index'),
	path('login', login, name='login'),
    # ex: /polls/5/results/
    path('register', register, name='register'),
    # ex: /polls/5/vote/
    path('about', about, name='about'),
    path('logout',logout, name='logout')
	]