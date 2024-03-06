"""
URL configuration for fakenews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from user import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.SignInView.as_view(), name='sign-in'),
    path('register/', views.SignUpView.as_view(), name='sign-up'),
    path('logout', views.SignOutView.as_view(), name='sign-out'),
    path('user/', views.UserIndexView.as_view(), name='user-home'),
    path('admin/', views.AdminIndexView.as_view(), name='admin-home'),
    path('user/profile/create',
         views.CreateUserProfileView.as_view(), name='profile-create'),
    path('user/profile/view/<int:pk>',
         views.UserProfileView.as_view(), name='profile-view'),
    path('user/profile/update/<int:pk>',
         views.UpdateUserProfileView.as_view(), name='profile-update'),
    path('user/profile/delete/<int:pk>',
         views.DeleteUserProfileView.as_view(), name='profile-delete'),
    path('user/request/new', views.NewRequestView.as_view(), name='new-request'),
    path('user/request/view/<int:pk>',
         views.DetailRequestView.as_view(), name='view-request'),
    path('user/request/delete/<int:pk>',views.DeleteRequestView.as_view(),name='delete-request'),
    path('user/request/edit/<int:pk>',views.UpdateRequestView.as_view(),name='edit-request'),
    path('list/users',views.UserListView.as_view(),name='list-user'),
    path('delete/user/<int:pk>',views.UserDeleteView.as_view(),name='delete-user'),
    path('update/request/<int:pk>',views.AdminUpdateRequestView.as_view(),name='update-request'),
    path('view/request/<int:pk>',views.AdminDetailRequestView.as_view(),name='admin-view-request')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
