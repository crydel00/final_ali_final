from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('post/add/', views.addPost, name='addPost'),
    path('post/view/<int:pk>/', views.postDetail, name='postDetail'),
    path('post/delete/<int:pk>/', views.deletePost, name='deletePost'),
    path('post/edit/<int:pk>/', views.editPost, name='editPost'),

    path('user/sign-up/', views.sign_up_page, name='sign_up_page'),
    path('user/login/', views.login_page, name='login_page'),
    path('user/logout/', views.logout_request, name='logout_request'),
]