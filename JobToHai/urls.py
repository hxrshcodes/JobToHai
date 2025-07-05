from django.contrib import admin
from django.urls import path
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('jobs/', jobs, name='jobs'),
    path('pricing/', pricing, name='pricing'),
    path('resume/', resume, name='resume'),
    path('makeresume/', makeresume, name='makeresume'),

    # LOGIN SYSTEM
    path('signup/',signup_page, name='signup'),
    path('login/', LogInUser, name='login'),
    path('logout/<int:pk>', user_logout, name='logout'),
    path('post_job/', post_job, name='post_job'),
    path('myprofile/', myprofile, name='profile'),
]
