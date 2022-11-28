from . import views
from django.urls import path 


urlpatterns = [
    path('',views.admin_login, name="login"),
    path('logout/',views.admin_logout, name="logout"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('users/', views.admin_users, name="adminusers"),
    path('product/', views.admin_products, name="adminproducts"),
    path('addproduct/', views.admin_addproduct, name="addproduct"),
    path('editproduct/<int:id>/',views.admin_editproduct, name="editproduct"),
    path('catagory/', views.admin_catagory, name="admincatagory"),
    path('addcatagory/',views.admin_addcatagory, name="addcatagory"),
    path('addsubcatagory/',views.admin_addsubcatagory, name="addsubcatagory"),
    path('editsubcatagory/<int:id>',views.admin_editsubcatagory, name="editsubcatagory"),
    path('editcatagory/<int:id>', views.admin_editcatagory, name="editcatagory"),
    path('deletecatagory/<int:id>', views.delete_catagory, name = "deletecatagory"),
    path('deleteproduct/<int:id>',views.admin_deleteproduct, name="deleteproduct"),
    path('blockuser/<int:id>',views.block_user, name="block"),
    path('unblockuser/<int:id>',views.unblock_user, name="unblock"),
    path('orders/',views.admin_orders,name="adminorders"),
    path('orderdetails/<int:id>',views.admin_order_details, name="orderdetails"),\
    path('orderstatus/<int:id>',views.order_status_change, name="statuschange")
]

