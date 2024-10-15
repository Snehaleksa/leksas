from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView




urlpatterns=[
    path('register',views.register),
    path('api/token/',TokenObtainPairView.as_view()),
]