from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'ore-inserite', views.ore_inseriteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]