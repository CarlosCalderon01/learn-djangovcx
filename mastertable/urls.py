# PACKAGES & LIBRARIES - THIRD
from django.urls import include, path
from rest_framework import routers
# PACKAGES & LIBRARIES - LOCAL
from mastertable import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls))
]

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section X - Task --> Temp
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
router.register(r'tasks', views.TaskView)
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 1 - Country, State, City, Neighborhood --> location
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
router.register(r'country', views.TaskView)
router.register(r'state', views.TaskView)
router.register(r'city', views.TaskView)
router.register(r'neighborhood', views.TaskView)
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 2 - Language --> Language
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
router.register(r'language', views.TaskView)
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 3 - GenderV01, GenderVX --> Genders
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
router.register(r'genderv01', views.TaskView)
router.register(r'gendervx', views.TaskView)
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 4 - HoliDay --> Days
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
router.register(r'holiday', views.TaskView)
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section X - X --> X
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //

# // ----- // ----- // ----- // Notes // ----- // ----- // ----- //
        
# // ----- // ----- // ----- // References // ----- // ----- // ----- //

# // ----- // ----- // ----- // Bibliography // ----- // ----- // ----- //
