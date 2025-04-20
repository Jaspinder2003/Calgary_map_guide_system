from rest_framework import serializers
from .models import *  # or wherever your model lives
from django.contrib.auth.hashers import make_password
from .models import Users


class CommunitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communities
        fields =  ['name', 'area', 'population']


class CrimeRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrimeRates
        fields = '__all__'

class DiningPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningPlaces
        fields = '__all__'

class EducationInstitutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationInstitutions
        fields = '__all__'

class HealthcareFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthcareFacilities
        fields = '__all__'

class RentalPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalPlaces
        fields = '__all__'

class SuperstoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superstores
        fields = '__all__'

class TransitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transit
        fields = '__all__'

class UniversitiesCollegesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversitiesColleges
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class UserQueriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQueries
        fields = '__all__'

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)

    def create(self, validated_data):
        return Users.objects.create(
            username = validated_data['username'],
            password = make_password(validated_data['password']),
            Email    = validated_data['email']
        )