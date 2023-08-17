from django.urls import path

from . import views

urlpatterns = [path("index",views.index,name="index"),
            path("productlist/<city>",views.productlist,name="productlist"),
            path("",views.login,name="login"),
            path("product/<hid>",views.product,name="product"),
            path("signup",views.signup,name="signup"),
            path("logout",views.logout,name="logout"),
            path("about",views.about,name="about"),
                                  
]    

