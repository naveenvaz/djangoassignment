from rest_framework import serializers
from .models import CustomUser,TodoTask

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTask
        fields = '__all__'
        read_only_fields = ['user']

    def validate(self, data):
        # Add your custom validation logic here
        user = self.context['user']
        name = data['name']
        description = data['description']

        # Check if a task with the same name and description exists for the current user
        existing_task = TodoTask.objects.filter(user=user, name=name, description=description).first()

        if existing_task:
            raise serializers.ValidationError(
                'A task with the same name and description already exists for the current user.')

        return data