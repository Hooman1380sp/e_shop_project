from django.urls import path
from . import views
urlpatterns = [
    path('add-p/',views.AddProductToCartView.as_view()),
    path('request-payment/', views.send_request, name='request'),
    path('verify-payment/', views.verify, name='verify'),
    path('receipt/',views.ReceiptOfMyShopView.as_view()),
]