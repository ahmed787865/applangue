from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='pk')
    phone = serializers.CharField(source='phone_number')
    password = serializers.CharField(write_only=True)
    name = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'phone', 'name', 'created_at', 'password']
        extra_kwargs = {'password': {'required': True}}

    def create(self, validated_data):
        user = self.Meta.model.objects.create_user(**validated_data)
        return user
