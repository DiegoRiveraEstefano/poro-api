from django.urls import path, include
from rest_framework.authtoken import views
from .views import (
    UserRegister,
)

user_urls = [
    #path("", ),
    path("register/", UserRegister.as_view()),
    #path("list/"),
    #path(":id/"),
]

urlpatterns = [
    path('api/v1/user/', include(user_urls)),
    path('api/v1/token/', views.obtain_auth_token),
]