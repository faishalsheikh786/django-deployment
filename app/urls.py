from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/register', views.register_user, name="register"),
    path('post/<slug:slug>', views.post_page, name="post_page"),
]
