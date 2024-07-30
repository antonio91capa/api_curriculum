from rest_framework import serializers
from .models import Education

# La forma en que vamos a mostrar los datos al API Rest
class EducationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            "pk",
            "data_ini",
            "date_end",
            "title",
        )

# La forma en que vamos a recibir esos datos y procesarlos
class EducationSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    date_ini = serializers.DateField()
    date_end = serializers.DateField(required=False)
    title = serializers.CharField(max_length=100)

    def create(self, data):
        education = Education.objects.create(**data)
        return education
