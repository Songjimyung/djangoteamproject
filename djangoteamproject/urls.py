"""
URL configuration for djangoteamproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from boards import views
from boards.views import Boards, BoardList, BoardDetail

# as_view()를 써야 cbv 방식을 fbv 처럼 쓸 수 있따.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),

    path('board/list/', BoardList.as_view(), name='board-list'),
    path('board/', Boards.as_view(), name='board-create'),
    path('board/<int:board_id>/', Boards.as_view(), name='board-delete'),
    path('board/<int:pk>/', BoardDetail.as_view(), name='board_detail'),
    path('board/edit/<int:pk>/', views.board_edit, name='board_edit'),

    # path('board/', views.board_create),
    # path('board/delete/<int:board_id>/', views.board_delete),
]
