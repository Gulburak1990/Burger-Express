
from django.urls import path
from rest_framework.routers import SimpleRouter
from main. views import BurgerViewSet


router = SimpleRouter()
router.register('', BurgerViewSet, basename='posts')



urlpatterns = router.urls

