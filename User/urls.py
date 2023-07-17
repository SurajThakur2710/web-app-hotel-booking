from django.urls import path
from . import views
from . import templates 
from django.urls.conf import include

urlpatterns = [
    path('Signup', views.signup,name="signup"),
    path('ForgotPassword', views.forgotPassword),
    path('login', views.Login,name="login"),
    # path('ChangePassword', views.changepassword),  
]


