from django.shortcuts import render
from rest_framework.authtoken.views import obtain_auth_token
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
from rest_framework.views import APIView
from .models import District
from django.core.serializers import serialize
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


def community_list(request):
    communities = Communities.objects.all()
    data = list(communities.values('name'),communities.values("Area",communities.values('Population')))  # Adjust fields as needed
    return JsonResponse(data, safe=False)


@csrf_exempt
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return JsonResponse({'error': 'Missing fields'}, status=400)

        email = email.lower().strip()

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'User already exists'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({
            'id': user.id,
            'username': user.username,
            'email': user.email
        }, status=201)

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

    def get_queryset(self):
        qs = EducationInstitutions.objects.all()
        t = self.request.query_params.get('type')
        if t in {'university','school'}:
            qs = qs.filter(type=t)
        return qs

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

class SchoolsViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolsSerializer


    
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
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated]
    serializer_class       = UserQueriesSerializer

    def get_queryset(self):
        # only this user’s queries
        return UserQueries.objects.filter(uid=self.request.user)

    def perform_create(self, serializer):
        # automatically associate new queries with the logged-in user
        serializer.save(uid=self.request.user)
        
        
class CommunityBoundariesViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = District
    
    
class AuthTokenViewSet(viewsets.ViewSet):
    
    def create(self, request):
        # simply call the DRF obtain_auth_token view under the hood:
        response = obtain_auth_token(request)
        # obtain_auth_token returns an HttpResponse,
        # so we need to forward its data and status
        return Response(response.data, status=response.status_code)