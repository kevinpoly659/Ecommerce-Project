from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name="home"),
    path('viewprod/<str:id>/', views.view_prod, name= "viewprod"),
]
