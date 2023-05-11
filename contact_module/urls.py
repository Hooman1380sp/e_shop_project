from django.urls import path
from .views import ContactUsView,AboutUsView


urlpatterns = [
    path('',ContactUsView.as_view()),
    path('about-us',AboutUsView.as_view()),
]