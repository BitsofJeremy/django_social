from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Login Page
    # path('login/', views.user_login, name='login'),
    # set main route to dashboard
    path('', views.dashboard, name='dashboard'),

    # Django provided auth workflow routes
    path('', include('django.contrib.auth.urls')),

    # or a manual setup of auth workflow routes
    # # User Login routes
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # # User change password routes
    # path(
    #     'password_change/',
    #     auth_views.PasswordChangeView.as_view(),
    #     name='password_change'
    # ),
    # path(
    #     'password_change/done/',
    #     auth_views.PasswordChangeDoneView.as_view(),
    #     name='password_change_done'
    # ),
    # # reset password routes
    # path(
    #     'password_reset/',
    #     auth_views.PasswordResetView.as_view(),
    #     name='password_reset'
    # ),
    # path(
    #     'password_reset/done/',
    #     auth_views.PasswordResetDoneView.as_view(),
    #     name='password_reset_done'
    # ),
    # path(
    #     'reset/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(),
    #     name='password_reset_confirm'
    # ),
    # path(
    #     'reset/done/',
    #     auth_views.PasswordResetCompleteView.as_view(),
    #     name='password_reset_complete'
    # ),
]

