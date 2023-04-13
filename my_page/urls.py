from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.view_users, name='home'),
    path('my-page/<int:id>/', views.my_page, name='my-page'),
    path('my-page/profile-modify/',views.update, name='profile-modify'),
]
