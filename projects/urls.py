from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"projects", views.ProjectViewSet, basename="projects")

# POST: /projects
# GET: /projects   /projects/<id>
# PUT: /projects/<id>
# DELETE: /projects/<id>
urlpatterns = [
    path("", include(router.urls)),
]
