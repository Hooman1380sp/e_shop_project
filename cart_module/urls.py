from django.urls import path
from .views import AddProductToCartView
urlpatterns = [
    path('add-p/',AddProductToCartView.as_view()),
]