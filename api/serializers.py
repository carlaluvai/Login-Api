from rest_framework import serializers, fields
from django.contrib.auth import get_user_model
from . models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['image', "id", "last_login", "is_superuser", "username", "first_name", "last_name",
                  "email", "is_staff", "is_active", "date_joined", "user_permissions", 'location', 'image']
        # lookup_field = 'username'
    
