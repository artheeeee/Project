from django.urls import include, path
from . import views
from . import api
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('info/', views.info, name='info'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('dashboard/',views.user_profile, name='dashboard'),
    path('donationbox/', views.request_box, name='box_sub'),
    path('envelope/', views.request_env, name='env_sub'),
    path('clothing/', views.clothing, name='clothing'),
    path('listbox/', views.listrequest_box, name="list_donationbox"),
    path('listenv/', views.listrequest_env, name="list_env"),
    path('listclothing/', views.list_clothing, name="list_clothing"),
    path('cashindex/', views.cashindex, name='cashindex'),
    path('charge/', views.charge, name='charge'),
    path('success/<str:args>/', views.successMsg, name='success'),
    path('success/<str:args>/', views.subsuccessMsg, name='subsuccess'),
]

urlpatterns += staticfiles_urlpatterns()
