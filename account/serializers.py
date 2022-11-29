from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={"input_type":"password"})
    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def save(self):
        password2 = self.validated_data.get("password2")
        password = self.validated_data.get("password")

        if password != password2:
            raise serializers.ValidationError({"error": "P1 and P2 must be same"})

        if User.objects.filter(email=self.validated_data.get("email")).exists():
            raise serializers.ValidationError({"error":"Email already exists!"})

        user = User(username=self.validated_data.get("username"), email=self.validated_data.get("email"))
        user.set_password(password)
        user.save()
        return user
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


