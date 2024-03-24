# PACKAGES & LIBRARIES - THIRD
from django.shortcuts import render
from rest_framework import viewsets
# PACKAGES & LIBRARIES - LOCAL
from .serializer import *
from .models import *

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section X - Task --> Temp
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //


class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 1 - Country, State, City, Neighborhood --> location
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //


class GmtCountryView(viewsets.ModelViewSet):
    serializer_class = GmtCountrySerializer
    queryset = GmtCountry.objects.all()


class GmtStateView(viewsets.ModelViewSet):
    serializer_class = GmtStateSerializer
    queryset = GmtState.objects.all()


class GmtCityView(viewsets.ModelViewSet):
    serializer_class = GmtCitySerializer
    queryset = GmtCity.objects.all()


class GmtNeighborhoodView(viewsets.ModelViewSet):
    serializer_class = GmtNeighborhoodSerializer
    queryset = GmtNeighborhood.objects.all()

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 2 - Language --> Language
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //


class GmtLanguageView(viewsets.ModelViewSet):
    serializer_class = GmtLanguageSerializer
    queryset = GmtLanguage.objects.all()

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 3 - GenderV01, GenderVX --> Genders
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //


class GmtGenderV01View(viewsets.ModelViewSet):
    serializer_class = GmtGenderV01Serializer
    queryset = GmtGenderV01.objects.all()


class GmtGenderVXView(viewsets.ModelViewSet):
    serializer_class = GmtGenderVXSerializer
    queryset = GmtGenderVX.objects.all()

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 4 - HoliDay --> Days
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //


class GmtHolidayView(viewsets.ModelViewSet):
    serializer_class = GmtHolidaySerializer
    queryset = GmtHoliday.objects.all()

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section X - X --> X
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //

# // ----- // ----- // ----- // Notes // ----- // ----- // ----- //

# // ----- // ----- // ----- // References // ----- // ----- // ----- //

# // ----- // ----- // ----- // Bibliography // ----- // ----- // ----- //
