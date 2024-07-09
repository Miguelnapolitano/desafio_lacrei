from django.urls import path, include
from rest_framework.routers import DefaultRouter
from visit.views import VisitViewSet

router = DefaultRouter()
router.register(r'visit', VisitViewSet, basename='visit')

urlpatterns = [
    path('', include(router.urls)),
]