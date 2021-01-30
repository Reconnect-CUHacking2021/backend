from rest_framework import serializers

from .models import Store, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["fields", "name", "phone", "vaccination_info"]
    
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ["name", "phone", "safety_policy", "location", "store_hours"]
    
    