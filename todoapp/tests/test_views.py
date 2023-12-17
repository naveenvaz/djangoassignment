import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from todoapp.models import TodoTask

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
    def _create_todo_task(user, **kwargs):
        return TodoTask.objects.create(user=user, **kwargs)
    return _create_todo_task

@pytest.mark.django_db
def test_welcome(api_client):
    response = api_client.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert response.content == b'Welcome to TodoApp!'


@pytest.mark.django_db
def test_register_user(api_client):
    user_data = {'username': 'naveenfirst', 'email': 'naveen111@example.com', 'password': '11111'}
    response = api_client.post('/api/register/', user_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_user_login(api_client, create_user):
    user = user = user = create_user(username='naveenfirst', email='naveen111@example.com', password='11111')
    login_data = {'username': 'naveenfirst', 'password': '11111'}
    response = api_client.post('/api/login/', login_data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'token' in response.data

@pytest.mark.django_db
def test_user_logout(api_client, create_user):
    user = create_user(username='testuser', email='testuser@example.com', password='testpassword')
    token = Token.objects.create(user=user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    response = api_client.post('/api/logout/')
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_create_todo_task(api_client, create_user):
    user = create_user(username='testuser', email='testuser@example.com', password='testpassword')
    token = Token.objects.create(user=user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    task_data = {'name': 'Test Task', 'description': 'Task description'}
    response = api_client.post('/api/tasks/create/', task_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_update_todo_task(api_client, create_user, create_todo_task):
    user = create_user(username='testuser', email='testuser@example.com', password='testpassword')
    task = create_todo_task(user=user, name='Old Task', description='Old Description')
    token = Token.objects.create(user=user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    update_data = {'name': 'Updated Task', 'description': 'Updated Description'}
    response = api_client.put(f'/api/tasks/update/{task.id}/', update_data, format='json')
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_delete_todo_task(api_client, create_user, create_todo_task):
    user = create_user(username='testuser', email='testuser@example.com', password='testpassword')
    task = create_todo_task(user=user, name='Task to Delete', description='Task Description')
    token = Token.objects.create(user=user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    response = api_client.delete(f'/api/tasks/delete/{task.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
