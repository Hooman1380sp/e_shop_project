from rest_framework import routers
from .views import *

app_name = 'admin_panel'
urlpatterns = [

]
router = routers.SimpleRouter()
router.register('user',UserViewSet,basename='user-panel')
router.register('product',ProductViewSet,basename='product-panel')
router.register('product-category',ProductCategoryViewSet,basename='product_category-panel')
router.register('product-visit',ProductVisitViewSet,basename='product_visit-panel')
router.register('contact-us',ContactUsViewSet,basename='contact_us-panel')
router.register('about-us',AboutUsViewSet,basename='about_us-panel')
router.register('cart',CartViewSet,basename='cart-panel')
router.register('cart-detail',CartDetailViewSet,basename='cart_detail-panel')
urlpatterns += router.urls

