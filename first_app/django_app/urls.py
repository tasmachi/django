from django.urls import path
from . import views

app_name='django_app'
urlpatterns=[
    path('',views.index,name='index'),
    path('signup/',views.register,name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('user_login/',views.user_login,name='user_login')
]