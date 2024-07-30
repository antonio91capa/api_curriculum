from rest_framework import serializers
from .models import Extra


class ExtraModelSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = ("pk", "expedition", "title", "url", "description")


class ExtraSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    expedition = serializers.DateField()
    title = serializers.CharField(max_length=30)
    url = serializers.URLField(required=False)
    description = serializers.CharField(max_length=200)

    def create(self, data):
        extra = Extra.objects.create(**data)
        return extra
