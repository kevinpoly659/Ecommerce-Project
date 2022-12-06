from . import views
from django.urls import path


urlpatterns = [
    path('ordercod/<int:id>',views.order_cod,name="ordercod"),
    path('razor_success/',views.razor_success,name="razor_success"),
    path('paypal_payment/<str:sum>/',views.paypal_payment, name="paypal_payment"),
    path('payment_done/', views.payment_done, name="payment_done"),
    path('payment_cancelled/', views.payment_cancelled, name="payment_cancelled"),
]
