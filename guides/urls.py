# Updated urls.py with relationship tables
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# Main model endpoints
router.register(r'communities', views.CommunityViewSet)
router.register(r'rentals', views.RentalPlacesViewSet)
router.register(r'education', views.EducationInstitutionsViewSet)
router.register(r'healthcare', views.HealthcareFacilitiesViewSet)
router.register(r'dining', views.DiningPlacesViewSet)
router.register(r'transit', views.TransitStopsViewSet)
router.register(r'superstores', views.SuperstoresViewSet)

# Relationship table endpoints
router.register(r'accessible-by', views.AccessibleByViewSet)
router.register(r'accessible-by-rental', views.AccessibleBy2ViewSet)
router.register(r'located-in', views.LocatedInViewSet)
router.register(r'located-near', views.LocatedNearViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]