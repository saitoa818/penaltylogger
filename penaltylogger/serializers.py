from django.contrib.auth.models import Judge
from rest_framework import serializers
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = '__all__'