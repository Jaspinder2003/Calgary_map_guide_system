# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (Community, RentalPlaces, EducationInstitutions,
                     HealthcareFacilities, DiningPlaces, TransitStops, Superstores, AccessibleBy, AccessibleBy2,
                     LocatedIn, LocatedNear)
from .serializers import (CommunitySerializer, RentalPlacesSerializer,
                          EducationInstitutionsSerializer, HealthcareFacilitiesSerializer,
                          DiningPlacesSerializer, TransitStopsSerializer, SuperstoresSerializer, AccessibleBySerializer,
                          AccessibleBy2Serializer, LocatedInSerializer, LocatedNearSerializer)

class CommunityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

from django.http import JsonResponse
from .models import RentalPlaces

def rental_places_geojson(request):
    features = []
    for place in RentalPlaces.objects.exclude(location=None):
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.location.x, place.location.y],
            },
            "properties": {
                "address": place.address,
                "type": place.type,
                "status": place.status
            },
        })
    return JsonResponse({"type": "FeatureCollection", "features": features})


class EducationInstitutionsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EducationInstitutions.objects.all()
    serializer_class = EducationInstitutionsSerializer

class HealthcareFacilitiesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HealthcareFacilities.objects.all()
    serializer_class = HealthcareFacilitiesSerializer

class DiningPlacesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DiningPlaces.objects.all()
    serializer_class = DiningPlacesSerializer

class TransitStopsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TransitStops.objects.all()
    serializer_class = TransitStopsSerializer

class SuperstoresViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Superstores.objects.all()
    serializer_class = SuperstoresSerializer


# Additional ViewSets for relationship tables
class AccessibleByViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AccessibleBy.objects.all()
    serializer_class = AccessibleBySerializer

    def get_queryset(self):
        queryset = AccessibleBy.objects.all()
        edu_address = self.request.query_params.get('edu_address', None)
        stop_id = self.request.query_params.get('stop_id', None)

        if edu_address is not None:
            queryset = queryset.filter(edu_address=edu_address)
        if stop_id is not None:
            queryset = queryset.filter(stop_id=stop_id)

        return queryset


class AccessibleBy2ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AccessibleBy2.objects.all()
    serializer_class = AccessibleBy2Serializer

    def get_queryset(self):
        queryset = AccessibleBy2.objects.all()
        rental_address = self.request.query_params.get('rental_address', None)
        stop_id = self.request.query_params.get('stop_id', None)

        if rental_address is not None:
            queryset = queryset.filter(rental_address=rental_address)
        if stop_id is not None:
            queryset = queryset.filter(stop_id=stop_id)

        return queryset


class LocatedInViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LocatedIn.objects.all()
    serializer_class = LocatedInSerializer

    def get_queryset(self):
        queryset = LocatedIn.objects.all()
        community_name = self.request.query_params.get('community_name', None)

        if community_name is not None:
            queryset = queryset.filter(community_name=community_name)

        return queryset


class LocatedNearViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LocatedNear.objects.all()
    serializer_class = LocatedNearSerializer

    def get_queryset(self):
        queryset = LocatedNear.objects.all()
        edu_address = self.request.query_params.get('edu_address', None)
        rental_address = self.request.query_params.get('rental_address', None)

        if edu_address is not None:
            queryset = queryset.filter(edu_address=edu_address)
        if rental_address is not None:
            queryset = queryset.filter(rental_address=rental_address)

        return queryset