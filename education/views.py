from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsStandardUser
from .serializers import EducationModelSerializer, EducationSerializer
from .models import Education


# Create your views here.
class EducationViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = EducationModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsStandardUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Education.objects.filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = EducationSerializer(
            data=request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        edu = serializer.save()
        data = EducationModelSerializer(edu).data
        return Response(data, status=status.HTTP_201_CREATED)
