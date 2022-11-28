from . import views
from django.urls import path


urlpatterns = [
    path('ordercod',views.order_cod,name="ordercod")
]
