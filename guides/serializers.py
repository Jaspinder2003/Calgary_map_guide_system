# serializers.py
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import (Community, RentalPlaces, EducationInstitutions, 
                    HealthcareFacilities, DiningPlaces, TransitStops, Superstores)

class CommunitySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Community
        geo_field = 'boundary'
        fields = ['name', 'population', 'community_structure', 'boundary']

class RentalPlacesSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RentalPlaces
        geo_field = 'location'
        fields = ['address', 'community_name', 'location', 'status', 'type']

class EducationInstitutionsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EducationInstitutions
        geo_field = 'location'
        fields = ['name', 'address', 'community_name', 'email', 'location', 
                 'phone_no', 'post_secondary', 'postal_code']

class HealthcareFacilitiesSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = HealthcareFacilities
        geo_field = 'location'
        fields = ['address', 'commnuity_name', 'location', 'name', 'type']

class DiningPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningPlaces
        fields = ['id', 'name', 'address', 'cuisine', 'rating']

class TransitStopsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TransitStops
        geo_field = 'location'
        fields = ['teleride_number', 'location', 'route_category', 
                 'route_long_name', 'route_short_name', 'status', 'stop_name']

class SuperstoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superstores
        fields = ['id', 'name', 'address']

# Additional serializers for relationship tables
from .models import AccessibleBy, AccessibleBy2, LocatedIn, LocatedNear

class AccessibleBySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessibleBy
        fields = ['edu_address', 'stop_id', 'distance_m']

class AccessibleBy2Serializer(serializers.ModelSerializer):
    class Meta:
        model = AccessibleBy2
        fields = ['rental_address', 'stop_id', 'distance_m']

class LocatedInSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocatedIn
        fields = ['community_name', 'route_name', 'stop_id', 'stop_name']

class LocatedNearSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocatedNear
        fields = ['edu_address', 'rental_address', 'distance_m']