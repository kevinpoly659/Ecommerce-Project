from . import views
from django.urls import path

urlpatterns = [
    path('addcart/<int:id>/',views.addcart, name="addcart"),
    path('viewcart/<int:disc>/', views.viewcart, name="viewcart"),
    path('deletecart/<int:id>/', views.deletecart, name="deletecart"),
    path('clearcart', views.clearcart, name="clearcart"),
    path('checkout/<str:sum>/', views.checkout, name="checkout"),
    path('add_quantity/<int:id>/', views.add_quantity, name="quantity"),
    path('down_quantity/<int:id>/', views.down_quantity, name="quantity"),
    path('applycoupon/<str:cod>/', views.apply_coupon,name="applycoupon"),
    
]
