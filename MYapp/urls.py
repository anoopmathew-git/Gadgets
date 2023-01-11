from django.urls import path
from MYapp import views

urlpatterns=[
    path('mainpage/',views.mainpage,name="mainpage"),
    path('addadminpage/', views.addadminpage, name="addadminpage"),
    path('adminsave/', views.adminsave, name="adminsave"),
    path('disadminpage/',views.disadminpage,name="disadminpage"),
    path('editpage/<int:dataid>/', views.editpage, name="editpage"),
    path('updatedata/<int:dataid>/', views.updatedata, name="updatedata"),
    path('deleteadmin/<int:dataid>/', views.deleteadmin, name="deleteadmin"),
    path('addcatpage/', views.addcatpage, name="addcatpage"),
    path('addcatsave/', views.addcatsave, name="addcatsave"),
    path('catdisplaypage/', views.catdisplaypage, name="catdisplaypage"),
    path('cateditpage/<int:dataid>/', views.cateditpage, name="cateditpage"),
    path('catupdate/<int:dataid>/', views.catupdate, name="catupdate"),
    path('deletecat/<int:dataid>/', views.deletecat, name="deletecat"),
    path('productpage/', views.productpage, name="productpage"),
    path('productsave/', views.productsave, name="productsave"),
    path('productdisplaypage/', views.productdisplaypage, name="productdisplaypage"),
    path('producteditpage/<int:dataid>/', views.producteditpage, name="producteditpage"),
    path('productupdate/<int:dataid>/', views.productupdate, name="productupdate"),
    path('deleteproduct/<int:dataid>/', views.deleteproduct, name="deleteproduct"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout")
    ]