from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'experience', views.ExperienceViewSet, basename="experience")

# POST: /experience
# GET: /experience   /experience/<id>
# PUT: /experience/<id>
# DELETE: /experience/<id>
urlpatterns = [
    path("", include(router.urls)),
]
