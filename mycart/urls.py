from . import views
from django.urls import path

urlpatterns = [
    path('addcart/<int:id>/',views.addcart, name="addcart"),
    path('viewcart', views.viewcart, name="viewcart"),
    path('deletecart/<int:id>/', views.deletecart, name="deletecart"),
    path('clearcart', views.clearcart, name="clearcart"),
    path('checkout/<str:sum>/', views.checkout, name="checkout")
]
