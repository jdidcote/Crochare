from django.urls import path, include

from patterns import views

urlpatterns = [
    path('create-pattern', views.create_pattern, name='create-pattern'),
    path('my-patterns', views.get_user_patterns, name='user-patterns'),
]