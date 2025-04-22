# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.gis.db import models




class Admins(models.Model):
    aid = models.AutoField(db_column='AID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Admins'


class Communities(models.Model):
    communityid = models.AutoField(db_column='CommunityID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=100, blank=True, null=True)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'Communities'



class CrimeRates(models.Model):
    crimeid = models.AutoField(db_column='CrimeID', primary_key=True)  # Field name made lowercase.
    communityid = models.OneToOneField(Communities, on_delete = models.CASCADE, db_column='CommunityID')  # Field name made lowercase.
    burglaryrate = models.DecimalField(db_column='BurglaryRate', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    scamrate = models.DecimalField(db_column='ScamRate', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    assaultrate = models.DecimalField(db_column='AssaultRate', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Crime_Rates'


class DiningPlaces(models.Model):
    diningid = models.AutoField(db_column='DiningID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ratings = models.DecimalField(db_column='Ratings', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Dining_Places'

class EducationInstitutions(models.Model):
    TYPE_CHOICES = [
        ('university', 'University / College'),
        ('school', 'School'),
    ]

    institution_id = models.AutoField(primary_key=True, db_column='InstitutionID')
    Name = models.CharField(max_length=255)
    NoOfStudents = models.IntegerField(default=0)
    Address = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    class Meta:
        db_table = 'Education_Institutions'

class HealthcareFacilities(models.Model):
    facilityid = models.AutoField(db_column='FacilityID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    communityid = models.ForeignKey(Communities,on_delete= models.CASCADE, db_column='CommunityID' )  # Field name made lowercase.
    
    class Meta:
        managed = True
        db_table = 'Healthcare_Facilities'




class RentalPlaces(models.Model):
    rentalid = models.AutoField(db_column='RentalID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rent = models.DecimalField(db_column='Rent', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    streetno = models.CharField(db_column='StreetNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    communityid = models.ForeignKey(Communities, on_delete=models.CASCADE, db_column='CommunityID' )  # Field name made lowercase.
    
    class Meta:
        managed = True
        db_table = 'Rental_Places'



class UniversitiesColleges(models.Model):
    # … any other fields …
    institution = models.OneToOneField(
        EducationInstitutions,
        on_delete=models.CASCADE,
        null=True,       # allow NULLs for existing rows
        blank=True       # allow blanks in forms/admin
    )
    name = models.CharField(max_length=255, default='Unknown University')
    number_of_students = models.IntegerField(default=0)
    
    class Meta:
        managed = True
        db_table = 'Universities_Colleges'

class School(models.Model):
    # Map the existing InstitutionID column as the PK
    institution = models.OneToOneField(
        EducationInstitutions,
        on_delete=models.CASCADE,
        db_column='InstitutionID',  # exactly your table’s column name
        primary_key=True            # tells Django “this is the PK—no 'id' field”
    )
    name = models.CharField(max_length=255, default='Unknown School')
    number_of_students = models.IntegerField(default=0)

    class Meta:
        db_table = 'schools'


class Superstores(models.Model):
    superstoreId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    open_hours = models.CharField(max_length=255, null=True, blank=True)  # For open hours
    type = models.CharField(max_length=255, null=True, blank=True)  # For store type
    
    class Meta:
        db_table = 'Superstores'  

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name


class Transit(models.Model):
    transitid = models.AutoField(db_column='TransitID', primary_key=True)  # Field name made lowercase.
    transitno = models.CharField(db_column='TransitNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    route = models.CharField(db_column='Route', max_length=100, blank=True, null=True)  # Field name made lowercase.
    endstop = models.CharField(db_column='EndStop', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Transit'



class UserQueries(models.Model):
    queryid = models.AutoField(db_column='QueryID', primary_key=True)  # Field name made lowercase.
    uid = models.ForeignKey('Users', models.CASCADE, db_column='UID')  # Field name made lowercase.
    querytext = models.CharField(db_column='QueryText', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'User_Queries'


class Users(models.Model):
   
    username = models.CharField(db_column='Username', unique=True, max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)  # Field name made lowercase.
    email = models.EmailField(db_column='email', max_length=50)  # Field name made lowercase.
  
    class Meta:
        managed = True
        db_table = 'Users'
    
    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower()
        super().save(*args, **kwargs)


class District(models.Model):
    name = models.CharField(max_length=100)
    class_code = models.IntegerField()
    comm_code = models.CharField(max_length=10)
    sector = models.CharField(max_length=20)
    sr_group = models.CharField(max_length=20)
    structure = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)
    
def __str__(self):
    return self.name


   