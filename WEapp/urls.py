from django.urls import path
from WEapp import views

urlpatterns=[

    path('webpage/', views.webpage, name="webpage"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contactus/',views.contactus,name="contactus"),
    path('discategory/<itemCatg>',views.discategory,name="discategory"),
    path('products/', views.products, name=" products"),
    path('productdetails/<int:dataid>', views.productdetails, name="productdetails"),
    path('weblogin/',views.weblogin,name="weblogin"),
    path('regdata/', views.regdata, name="regdata"),
    path('customerlogin/', views.customerlogin, name="customerlogin"),
    path('userlogout/', views.userlogout, name="userlogout")
]