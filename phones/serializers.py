from .models import mobile
from rest_framework import serializers

class mobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = mobile
        fields = "__all__"