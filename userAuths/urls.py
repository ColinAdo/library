from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    # auth url
    path('register/', views.sign_up, name="sign_up"),
    path('login/', views.sign_in, name="sign_in"),
    path('logout/', views.sign_out, name="sign_out"),

    # profile url
    path('<str:username>/profile/', views.profile, name="profile"),
    path('<str:username>/settings/', views.setting, name="setting"),

    # Password reset url 
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html'), name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), name="password_reset_complete"),
]