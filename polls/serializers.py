from rest_framework.serializers import ModelSerializer
from .models import TeacherModel
class TeacherSerializer(ModelSerializer):
    class Meta:
        model=TeacherModel
        fields=('__all__')
