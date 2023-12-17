from django.contrib import admin
from django.urls import path, include
from todoapp.views import welcome
urlpatterns = [
    path('', welcome, name='welcome'),
    path('admin/', admin.site.urls),
    path('api/', include('todoapp.urls')),
]
