from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProductListView.as_view()),
    path('most-visit/',views.MostVisitProductView.as_view()),
    path('productdetail/<slug:slug>/',views.ProductDetailView.as_view()),
    path('productcategorylist/',views.ProductCategoryListView.as_view()),
    path('productcategorydetail/<slug:slug>/',views.ProductCategoryDetailView.as_view()),

]