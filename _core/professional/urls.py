from django.urls import path, include
from rest_framework.routers import DefaultRouter
from professional.views import ProfessionalViewSet

router = DefaultRouter()
router.register(r'professional', ProfessionalViewSet, basename='professional')

urlpatterns = [
    path('', include(router.urls)),
]
