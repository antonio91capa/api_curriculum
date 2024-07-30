from django.urls import path
from .views import Post_APIView, Post_APIView_Detail

app_name = "api"

urlpatterns = [
    path("v1/post", Post_APIView.as_view()),
    path("v1/post/<int:pk>/", Post_APIView_Detail.as_view()),
]
