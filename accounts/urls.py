from django.urls import path
from accounts.views import *

from django.contrib.auth import views as authViews 
from django.contrib.auth import views as auth_views



urlpatterns = [
   	
      path('profile/edit', EditProfile, name='edit-profile'),
   	path('signup/', Signup, name='signup'),
   	#path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
      path('login/', login_user, name='login'),
   	path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
   	path('changepassword/', PasswordChange, name='change_password'),
   	path('changepassword/done', PasswordChangeDone, name='change_password_done'),
   	path('passwordreset/', authViews.PasswordResetView.as_view(), name='password_reset'),
   	path('passwordreset/done', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
   	path('passwordreset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   	path('passwordreset/complete/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


      path('changepasswordadmin/', PasswordChangeAdmin, name='change_password_admin'),



      path('reset_password/', auth_views.PasswordResetView.as_view(template_name='home/password_reset.html'), name='reset_password'),
      path('reset_email_sent/', auth_views.PasswordResetDoneView.as_view(template_name='home/password_reset_done.html'), name='password_reset_done'),
      path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='home/password_reset_confirm.html'), name='password_reset_confirm'),
      path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='home/password_reset_complete.html'), name='password_reset_complete'),


]