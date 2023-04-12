from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.view_users, name='home'),
    path('my-page/<int:id>/', views.my_page, name='my-page'),
]
