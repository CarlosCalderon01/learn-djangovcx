# PACKAGES & LIBRARIES - THIRD
from rest_framework import serializers
# PACKAGES & LIBRARIES - LOCAL
from .models import *

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section X - Task --> Temp
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 1 - Country, State, City, Neighborhood --> location
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //


class GmtCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GmtCountry
        fields = '__all__'


class GmtStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GmtState
        fields = '__all__'


class GmtCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = GmtCity
        fields = '__all__'


class GmtNeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = GmtNeighborhood
        fields = '__all__'

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 2 - Language --> Language
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //


class GmtLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GmtLanguage
        fields = '__all__'

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 3 - GenderV01, GenderVX --> Genders
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //


class GmtGenderV01Serializer(serializers.ModelSerializer):
    class Meta:
        model = GmtGenderV01
        fields = '__all__'


class GmtGenderVXSerializer(serializers.ModelSerializer):
    class Meta:
        model = GmtGenderVX
        fields = '__all__'

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 4 - HoliDay --> Days
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //


class GmtHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = GmtHoliday
        fields = '__all__'

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section X - X --> X
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //

# // ----- // ----- // ----- // Notes // ----- // ----- // ----- //

# // ----- // ----- // ----- // References // ----- // ----- // ----- //

# // ----- // ----- // ----- // Bibliography // ----- // ----- // ----- //

# Serialized --> https://www.django-rest-framework.org/api-guide/serializers/

# ForeignKey

    # utilizando los serializers relacionados.
