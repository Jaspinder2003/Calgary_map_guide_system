# CPSC471CalgaryGuidesystem/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from guides.views import *
from rest_framework.authtoken.views import obtain_auth_token


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
router.register(r'community-boundaries', CommunityBoundariesViewSet, basename='community-boundaries')
router.register(r'user-queries', UserQueriesViewSet, basename='user-queries')
router.register(r'api-token-auth', AuthTokenViewSet, basename='api-token-auth')


urlpatterns = [      
      path('admin/', admin.site.urls),
      path('api/', include(router.urls)),
]