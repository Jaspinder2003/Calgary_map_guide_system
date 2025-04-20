from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from .serializers import CommunitiesSerializer
from guides.models import Communities
from django.http import JsonResponse
from .models import Communities
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets , status
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from rest_framework.decorators import action



def community_list(request):
    communities = Community.objects.all()
    data = list(communities.values('name'),communities.values("Area",communities.values('Population')))  # Adjust fields as needed
    return JsonResponse(data, safe=False)

@csrf_exempt
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('email')
        password = data.get('password')

        if not username or not password:
            return JsonResponse({'error': 'Missing fields'}, status=400)

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'User already exists'}, status=400)

        # Create the user
        user = User.objects.create_user(username=username, password=password)

        return JsonResponse({'id': user.id}, status=201)

    return JsonResponse({'error': 'Invalid method'}, status=405)



class CommunitiesViewSet(viewsets.ModelViewSet):
    queryset = Communities.objects.all()
    serializer_class = CommunitiesSerializer

class CrimeRatesViewSet(viewsets.ModelViewSet):
    queryset = CrimeRates.objects.all()
    serializer_class = CrimeRatesSerializer

class DiningPlacesViewSet(viewsets.ModelViewSet):
    queryset = DiningPlaces.objects.all()
    serializer_class = DiningPlacesSerializer

class EducationInstitutionsViewSet(viewsets.ModelViewSet):
    queryset = EducationInstitutions.objects.all()
    serializer_class = EducationInstitutionsSerializer

class HealthcareFacilitiesViewSet(viewsets.ModelViewSet):
    queryset = HealthcareFacilities.objects.all()
    serializer_class = HealthcareFacilitiesSerializer

class RentalPlacesViewSet(viewsets.ModelViewSet):
    queryset = RentalPlaces.objects.all()
    serializer_class = RentalPlacesSerializer

class SuperstoresViewSet(viewsets.ModelViewSet):
    queryset = Superstores.objects.all()
    serializer_class = SuperstoresSerializer

class TransitViewSet(viewsets.ModelViewSet):
    queryset = Transit.objects.all()
    serializer_class = TransitSerializer

class UniversitiesCollegesViewSet(viewsets.ModelViewSet):
    queryset = UniversitiesColleges.objects.all()
    serializer_class = UniversitiesCollegesSerializer

    
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer  # Default serializer

    @action(detail=False, methods=['post'], url_path='register', serializer_class=RegisterSerializer)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'id': user.id}, status=status.HTTP_201_CREATED)

class UserQueriesViewSet(viewsets.ModelViewSet):
    queryset = UserQueries.objects.all()
    serializer_class = UserQueriesSerializer
