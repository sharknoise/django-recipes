from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.RecipesListView.as_view(), name='recipes_list'),
]