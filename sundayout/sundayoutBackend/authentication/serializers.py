from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ('id', 'firstName', 'lastName', 'email', 'password', 'createdAt')
        read_only_fields = ('createdAt',)

    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            firstName = validated_data['firstName'],
            lastName = validated_data['lastName'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user