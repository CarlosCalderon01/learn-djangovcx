# PACKAGES & LIBRARIES - THIRD
from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
# PACKAGES & LIBRARIES - LOCAL
from mastertable import views

router = routers.DefaultRouter()

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section X - Task --> Temp
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
router.register(r'tasks', views.TaskView)
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 1 - Country, State, City, Neighborhood --> location
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
router.register(r'country', views.GmtCountryView)
router.register(r'state', views.GmtStateView)
router.register(r'city', views.GmtCityView)
router.register(r'neighborhood', views.GmtNeighborhoodView)
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 2 - Language --> Language
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
router.register(r'language', views.GmtLanguageView)
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 3 - GenderV01, GenderVX --> Genders
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
router.register(r'genderv01', views.GmtGenderV01View)
router.register(r'gendervx', views.GmtGenderVXView)
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 4 - HoliDay --> Days
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
router.register(r'holiday', views.GmtHolidayView)
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section X - X --> X
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //

# mastertable/
urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title="mastertable API"))
]

# // ----- // ----- // ----- // Notes // ----- // ----- // ----- //
        
# // ----- // ----- // ----- // References // ----- // ----- // ----- //

# // ----- // ----- // ----- // Bibliography // ----- // ----- // ----- //
