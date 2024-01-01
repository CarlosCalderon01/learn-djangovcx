# PACKAGES & LIBRARIES - THIRD
from django.db import models
# PACKAGES & LIBRARIES - LOCAL

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section X - Task --> Temp
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //

class Task(models.Model):
    # id = models.AutoField()
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Task'
    
    def __str__(self):
        return self.title

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 1 - Country, State, City, Neighborhood --> location
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //

class GmtCountry(models.Model):
    name = models.TextField()
    alfa2 = models.CharField(max_length=2, blank=True, null=True)
    alfa3 = models.CharField(max_length=3, blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    num = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmtcountry'

class GmtState(models.Model):
    gmtcountry = models.ForeignKey('Gmtcountry', models.DO_NOTHING)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'gmtstate'


class GmtCity(models.Model):
    gmtstate = models.ForeignKey('Gmtstate', models.DO_NOTHING)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'gmtcity'

class GmtNeighborhood(models.Model):
    gmtcity = models.ForeignKey('gmtcity', models.DO_NOTHING)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'gmtneighborhood'

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 2 - Language --> Language
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //

class GmtLanguage(models.Model):
    name = models.TextField()
    iso6391 = models.CharField(max_length=2, blank=True, null=True)
    iso6392 = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmtlanguage'

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 3 - GenderV01, GenderVX --> Genders
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //

class GmtGenderV01(models.Model):
    id = models.BooleanField(primary_key=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    idchar = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmtgenderv01'


class GmtGenderVX(models.Model):
    name = models.TextField(unique=True)
    idchar = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmtgendervx'

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 4 - HoliDay --> Days
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
        
class GmtHoliday(models.Model):
    gmtcountry = models.ForeignKey('Gmtcountry', models.DO_NOTHING)
    holiday = models.DateField(unique=True)
    titleday = models.TextField(blank=True, null=True)
    descriptionday = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmtholiday'

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section X - X --> X
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //

# // ----- // ----- // ----- // Notes // ----- // ----- // ----- //
        
# // ----- // ----- // ----- // References // ----- // ----- // ----- //

# // ----- // ----- // ----- // Bibliography // ----- // ----- // ----- //
