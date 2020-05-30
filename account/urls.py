
from django.urls import path,include
from django import .views   
    
    
      
    
urlpatterns = [
    path("/login", views.login_view, name="login"),
    path("/logout", views.logout_view, name="logout"),
]