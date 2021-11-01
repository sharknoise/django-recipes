import django_filters
from django.db import models
from recipes.models import Ingredient, Recipe


class RecipeFilter(django_filters.FilterSet):
    """Filter by ingredient and by recipe name."""

    ingredients = django_filters.ModelChoiceFilter(
        queryset=Ingredient.objects.all()
    )
    class Meta:
        model = Recipe
        fields = ['name']

        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }