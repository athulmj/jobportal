from django.urls import path
from users import views

urlpatterns=[
    path("accounts/signup",views.SignUpView.as_view(),name='signup'),
    path("", views.SignInView.as_view(),name='signin'),
    path("accounts/signout", views.signout,name="signout")
]