from . import views
from django.urls import path


urlpatterns = [
path('user_login',views.user_login,name='login'),    
]

