from rest_framework import serializers

from .models import Store, User, Code

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["pk", "username", "email", "name", "phone", "vaccination_info"]
    
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ["pk", "name", "phone", "safety_policy", "location", "store_hours"]
    

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ["uuid", "user", "store"]
