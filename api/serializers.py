from rest_framework import serializers
from api import models

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mem
        fields = '__all__'

