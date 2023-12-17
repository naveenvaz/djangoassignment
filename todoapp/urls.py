from django.urls import path
from .views import register_user, user_login, user_logout,create_todo_task,update_todo_task,delete_todo_task,welcome

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('tasks/create/', create_todo_task, name='create_todo_task'),
    path('tasks/update/<int:task_id>/', update_todo_task, name='update_todo_task'),
    path('tasks/delete/<int:task_id>/', delete_todo_task, name='delete_todo_task'),
]