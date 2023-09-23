from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.sign_up, name="sign_up"),
    path('login/', views.sign_in, name="sign_in"),
    path('logout/', views.sign_out, name="sign_out"),
]