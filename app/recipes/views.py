from django.views.generic import ListView
from recipes.models import Recipe


class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes-list.html'
