from django.urls import path
from . import views
urlpatterns = [
    path('account/signup', views.signup, name='signup'),
    path('account/signin', views.signin, name='signin'),
    path('account/signout', views.signout, name='signout'),
]