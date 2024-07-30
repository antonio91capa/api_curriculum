from rest_framework import serializers
from .models import Project


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("pk", "date", "title", "url", "description")


class ProjectSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    date = serializers.DateField()
    title = serializers.CharField(max_length=30)
    url = serializers.URLField(required=False)
    description = serializers.CharField(max_length=200)

    def create(self, data):
        pro = Project.objects.create(**data)
        return pro
