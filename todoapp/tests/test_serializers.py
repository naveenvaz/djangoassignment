import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from todoapp.models import TodoTask
from todoapp.serializers import UserSerializer, TodoTaskSerializer

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    def _create_user(**kwargs):
        return get_user_model().objects.create_user(**kwargs)
    return _create_user

@pytest.fixture
def create_todo_task(create_user):
    def _create_todo_task(user, name='Test Task', description='Task description', **kwargs):
        existing_task = TodoTask.objects.filter(user=user, name=name, description=description).first()

        if existing_task:
            raise ValueError('A task with the same name and description already exists for the current user.')

        return TodoTask.objects.create(user=user, name=name, description=description, **kwargs)

    return _create_todo_task

@pytest.mark.django_db
def test_user_serializer(api_client, create_user):
    user_data = {'username': 'testuser', 'email': 'testuser@example.com', 'password': 'testpassword'}
    serializer = UserSerializer(data=user_data)
    assert serializer.is_valid()
    user = serializer.save()
    assert user.username == user_data['username']
    assert user.email == user_data['email']
    assert user.check_password(user_data['password'])

from datetime import datetime, timezone
@pytest.mark.django_db
def test_todo_task_serializer(api_client, create_user):
    user = create_user(username='testuser', email='testuser@example.com', password='testpassword')
    deadline_str = '2023-12-31T23:59:59Z'
    task_data = {
        'name': 'Test Task',
        'description': 'Task description',
        'deadline': deadline_str,
    }
    serializer = TodoTaskSerializer(data=task_data, context={'user': user})
    assert serializer.is_valid()
    task = serializer.save(user=user)
    assert task.name == task_data['name']
    assert task.description == task_data['description']
    expected_deadline = datetime.fromisoformat(deadline_str).replace(tzinfo=timezone.utc)
    assert task.deadline == expected_deadline