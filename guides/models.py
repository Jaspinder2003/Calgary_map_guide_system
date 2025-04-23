from django.db import models
from django.contrib.gis.db import models

class Admin(models.Model):
    admin_id = models.CharField(primary_key=True, max_length=255)
    email = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'admin'

class Community(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    population = models.IntegerField(null=True)
    community_structure = models.CharField(max_length=255, null=True)
    boundary = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'community'

class CrimeStatistics(models.Model):
    community_name = models.ForeignKey(Community, on_delete=models.CASCADE, db_column='community_name')
    crime_count = models.IntegerField(null=True)
    category = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'crime_statistics'

class DiningPlaces(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    cuisine = models.CharField(max_length=255, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    class Meta:
        db_table = 'dining_places'

class EducationInstitutions(models.Model):
    name = models.CharField( max_length=255)
    address = models.CharField(primary_key=True, max_length=255)
    community_name = models.ForeignKey(Community, on_delete=models.CASCADE, db_column='community_name', null=True)
    email = models.CharField(max_length=255, null=True)
    location = models.PointField(srid=4326, null=True)
    phone_no = models.CharField(max_length=255, null=True)
    post_secondary = models.BooleanField(null=True)
    postal_code = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'education_institutions'
        unique_together = (('name', 'address'),)

class HealthcareFacilities(models.Model):
    address = models.CharField(primary_key=True, max_length=255)
    commnuity_name = models.CharField(max_length=255, null=True)  # Note typo in DB column
    location = models.PointField(srid=4326)
    name = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'healthcare_facilities'

class TransitStops(models.Model):
    teleride_number = models.IntegerField(primary_key=True)
    location = models.PointField(srid=4326, null=True)
    route_category = models.CharField(max_length=255, null=True)
    route_long_name = models.CharField(max_length=255, null=True)
    route_short_name = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    stop_name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'transit_stops'

class LocatedIn(models.Model):
    community_name = models.ForeignKey(Community, on_delete=models.CASCADE, db_column='community_name')
    route_name = models.CharField(max_length=255)
    stop_id = models.IntegerField()
    stop_name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'located_in'
        unique_together = (('community_name', 'route_name', 'stop_id'),)


class RentalPlaces(models.Model):
    address = models.CharField(primary_key=True, max_length=255)
    community_name = models.ForeignKey(Community, on_delete=models.CASCADE, db_column='community_name', null=True)
    location = models.PointField(srid=4326, null=True)
    status = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'rental_places'

class AccessibleBy(models.Model):
    edu_address = models.CharField(max_length=255)
    stop_id = models.IntegerField()
    distance_m = models.IntegerField(null=True)

    class Meta:
        db_table = 'accessible_by'
        unique_together = (('edu_address', 'stop_id'),)

class AccessibleBy2(models.Model):
    rental_address = models.CharField(max_length=255)
    stop_id = models.IntegerField()
    distance_m = models.IntegerField(null=True)

    class Meta:
        db_table = 'accessible_by_2'
        unique_together = (('rental_address', 'stop_id'),)


class LocatedNear(models.Model):
    edu_address = models.CharField(max_length=255)
    rental_address = models.CharField(max_length=255)
    distance_m = models.IntegerField(null=True)

    class Meta:
        db_table = 'located_near'
        unique_together = (('edu_address', 'rental_address'),)


class Superstores(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'superstores'

class User(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    email = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'user'