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
    path('orderdetails/<int:id>',views.admin_order_details, name="orderdetails"),
    path('orderstatus/<int:id>',views.order_status_change, name="statuschange"),
    path('salesreport', views.sales_report, name="salesreport"),
    path('monthlysales', views.monthly_sales, name="monthlysales"),
    path('yearly_sales', views.yearly_sales,  name="yearlysales"),
    path('', views.main_view, name="main-view"),
    path('coupon/', views.admin_coupon, name="coupon"),
    path('addcoupon', views.add_coupon, name="addcoupon"),
    path('offers/',views.admin_offers,name="offers"),
    path('add_product_offer/',views.add_product_offer,name="add_product_offer"),
    path('delete_product_offer/<int:id>',views.delete_product_offer,name="delete_product_offer"),
    path('add_catagory_offer/',views.add_catagory_offer,name="add_catagory_offer"),
    path('delete_catagory_offer/<int:id>', views.delete_catagory_offer,name="delete_catagory_offer"),
]

