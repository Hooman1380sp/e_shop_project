from django.urls import path
from .views import ContactUsView, AboutUsView

app_name = 'contact_us'
urlpatterns = [
    path('',ContactUsView.as_view()),
    path('about-us',AboutUsView.as_view()),
]