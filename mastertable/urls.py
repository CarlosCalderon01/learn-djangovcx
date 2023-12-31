from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from mastertable import views

router = routers.DefaultRouter()
router.register(r'task1', views.TaskView)

urlpatterns = [
    path('', include(router.urls))
]
