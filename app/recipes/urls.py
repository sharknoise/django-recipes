from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.RecipesListView.as_view(), name='recipes_list'),
    path('', views.RecipesListView.as_view(), name='recipes_list'),
    path('<int:pk>/', views.RecipeDetailedView.as_view(), name='recipe_detailed'),
]