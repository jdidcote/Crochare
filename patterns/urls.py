from django.urls import path, include

from patterns import views

urlpatterns = [
    path('create-pattern', views.create_pattern, name='create-pattern'),
    path('edit-pattern/<int:pattern_id>', views.edit_pattern, name='edit-pattern'),
    path('my-patterns', views.get_user_patterns, name='user-patterns'),
    path('my-patterns/delete/<int:pattern_id>', views.delete_pattern, name='delete-pattern')
]