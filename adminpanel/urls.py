from . import views
from django.urls import path 


urlpatterns = [
    path('login/',views.admin_login, name="login"),
    path('logout/',views.admin_logout, name="logout"),
    path('dashboard/',views.dashboard, name="dashboard"),
]

