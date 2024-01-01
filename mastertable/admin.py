# PACKAGES & LIBRARIES - THIRD
from django.contrib import admin
# PACKAGES & LIBRARIES - LOCAL
from .models import *

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section X - Task --> Temp
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //

admin.site.register(Task)

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 1 - Country, State, City, Neighborhood --> location
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //

admin.site.register(GmtCountry)
admin.site.register(GmtState)
admin.site.register(GmtCity)
admin.site.register(GmtNeighborhood)

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 2 - Language --> Language
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //

admin.site.register(GmtLanguage)

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 3 - GenderV01, GenderVX --> Genders
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //

admin.site.register(GmtGenderV01)
admin.site.register(GmtGenderVX)

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section 4 - HoliDay --> Days
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
        
admin.site.register(GmtHoliday)

# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //
# Section X - X --> X
# // ----- // ----- // ----- // ----- // ----- // ----- // ----- //

# // ----- // ----- // ----- // Notes // ----- // ----- // ----- //
        
# // ----- // ----- // ----- // References // ----- // ----- // ----- //

# // ----- // ----- // ----- // Bibliography // ----- // ----- // ----- //
