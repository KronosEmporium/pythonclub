from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getresources/', views.getresources, name = 'resources'),
    path('getmeetings/', views.getmeetings, name = 'meetings'),
    path('getminutes/', views.getminutes, name = 'minutes'),
    path('getevents/', views.getevents, name = 'events'),
    path('meetingdetails/<int:id>', views.meetingdetails, name = 'meetingdetails'),
    path('newMeeting/', views.newMeeting, name = 'newmeeting'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]