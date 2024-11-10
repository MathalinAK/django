

from django.contrib import admin
from django.urls import path
from . import views
from .views import (
    loginView, forgot_passwordView, reset_passwordView, registerprocessView, 
    changepasswordView,logoutView,aboutusView,home1View,editprofileView, profileView,productView,productsView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginView.as_view(), name='login'), 
    path('forgot-password/', forgot_passwordView.as_view(), name='forgot_password'), 
    path('reset-password/', reset_passwordView.as_view(), name='reset_password'),  
    path('registerprocess/', registerprocessView.as_view(), name='registerprocess'),  
    path('aboutus/', aboutusView.as_view(), name='aboutus'),  
    path('home/', home1View.as_view(), name='home1'), 
    path('changepassword/', changepasswordView.as_view(), name='changepassword'), 
    path('editprofile/',editprofileView.as_view(), name='editprofile'), 
    path('logout/', logoutView.as_view(), name='logout'), 
    path('profile/', profileView.as_view(), name='profile'),
    path('product/',productView.as_view(),name='product'),
    path('products/',productsView.as_view(),name='products'),
    
]

