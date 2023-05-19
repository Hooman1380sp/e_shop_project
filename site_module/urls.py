from django.urls import path
from .views import *

urlpatterns = [
    path('p-l',SiteBannerProductListView.as_view()),
    path('p-d',SiteBannerProductDetailView.as_view()),
    path('pc-l',SiteBannerCategoryListView.as_view()),
    path('pc-d',SiteBannerCategoryDetailView.as_view()),
    path('a-us',SiteBannerAboutUsView.as_view()),
    path('index',SiteBannerIndexPageView.as_view()),
]