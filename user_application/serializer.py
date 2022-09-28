from rest_framework import serializers
from user_application.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def validate(self, data):
        if data['email'][0]:
            for n in data['email'][0]:
                if n.isdigit():
                    raise serializers.ValidationError({"error":"Email must start with alphabet's "})


        return data