from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users import views as user_views

router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')

# /users/login/
# /users/signup/
urlpatterns = [
    path('', include(router.urls)),
]
