from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from .models import Store, User, Code, VACCINATION_CHOICES
from allauth.utils import (email_address_exists,
                            get_username_max_length)

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

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    name = serializers.CharField(max_length=128)
    phone = serializers.CharField(max_length=32)
    vaccination_info = serializers.ChoiceField(choices=VACCINATION_CHOICES)
    is_store_owner = serializers.BooleanField(default=False)


    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    ("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user, data):
        user.name = data['name']
        user.phone = data['phone']
        user.is_store_owner = data['is_store_owner']
        user.save()

    def get_cleaned_data(self):
        print(self.validated_data)
        return {
            'username': self.validated_data.get('username', ''),
            'name': self.validated_data.get('name', ''),
            'phone': self.validated_data.get('phone', ''),
            'is_store_owner': self.validated_data.get('is_store_owner', False),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user, self.cleaned_data)
        setup_user_email(request, user, [])
        return user

