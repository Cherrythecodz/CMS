from django.urls import path
from .views import create_order, register

urlpatterns = [
    path('frontend\src\Pages\CreateOrder.js', create_order, name='CreateOrder'),
    path('frontend\src\Pages\Register.js', register, name='Register' ),
]
