"""
URL configuration for api_curriculum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("pruebarest.urls")),
    path("", include(("users.urls", "users"), namespace="users")),
    path("api/", include(("experiences.urls", "experiences"), namespace="experiences")),
    path("api/", include(("education.urls", "education"), namespace="educations")),
    path("api/", include(("projects.urls", "projects"), namespace="projects")),
    path("api/", include(("extras.urls", "extras"), namespace="extras")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
