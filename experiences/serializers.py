from rest_framework import serializers
from .models import Experience


class ExperienceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = (
            "pk",
            "date_ini",
            "date_end",
            "company",
            "description",
        )

class ExperienceSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    date_ini = serializers.DateTimeField()
    date_end = serializers.DateTimeField(required=False)
    company = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)

    def create(self, data):
        exp = Experience.objects.create(**data)
        return exp
