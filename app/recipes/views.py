
from django.views.generic import DetailView
from django_filters.views import FilterView
from recipes.filters import RecipeFilter
from recipes.models import Recipe


class RecipesListView(FilterView):
    model = Recipe
    template_name = 'recipes-list.html'
    filterset_class = RecipeFilter


class RecipeDetailedView(DetailView):
    model = Recipe
    template_name = 'recipe-detailed.html'
