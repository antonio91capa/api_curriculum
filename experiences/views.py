from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsStandardUser
from .serializers import ExperienceModelSerializer, ExperienceSerializer

from .models import Experience


# Create your views here.
class ExperienceViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ExperienceModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsStandardUser]
        return [permission() for permission in permission_classes]

    # Crea una nueva experiencia del usuario
    def create(self, request, *args, **kwargs):
        serializer = ExperienceSerializer(
            data=request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        experience = serializer.save()
        data = ExperienceModelSerializer(experience).data
        return Response(data, status=status.HTTP_201_CREATED)

    # Obtiene todaas las experiencias del usuario
    def get_queryset(self):
        queryset = Experience.objects.filter(user=self.request.user)
        return queryset
