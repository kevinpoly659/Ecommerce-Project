from . import views
from django.urls import path


urlpatterns = [
path('',views.user_login,name='userlogin'),    
path('account/',views.user_account,name = 'account'),
path('user_view_order/<int:id>',views.user_view_order, name="vieworder"),
path('user_return_order/<int:id>',views.user_return_order, name="return_order"),
path('user_cancel_order/<int:id>',views.user_cancel_order, name="cancel_order"),
path('addadress/',views.user_add_address,name="addaddress"),
path('delete_address/<int:id>',views.delete_address,name="delete_address"),
path('signup/',views.user_signup, name='usersignup'),
path('logout',views.user_logout,name='userlogout'),
path('user_otp_login', views.user_otp_login, name='otplogin'),
path('otp_verify', views.otp, name='otpverify'),
path('user_edit_account',views.user_edit_account, name="user_edit_account")
]

