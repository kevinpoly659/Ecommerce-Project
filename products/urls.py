from . import views
from django.urls import path


urlpatterns = [
    path('products/<str:id1>/<str:id2>/',views.product, name="products")
]

