# CPSC471CalgaryGuidesystem/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from guides.views import *


router = DefaultRouter()
router.register(r'communities', CommunitiesViewSet)
router.register(r'crime-rates', CrimeRatesViewSet)
router.register(r'dining-places', DiningPlacesViewSet)
router.register(r'education-institutions', EducationInstitutionsViewSet)
router.register(r'healthcare-facilities', HealthcareFacilitiesViewSet)
router.register(r'rental-places', RentalPlacesViewSet)
router.register(r'superstores', SuperstoresViewSet)
router.register(r'transit', TransitViewSet)
router.register(r'users', UsersViewSet)
router.register(r'user-queries', UserQueriesViewSet)



urlpatterns = [      
      path('admin/', admin.site.urls),
      path('api/', include(router.urls)),
]