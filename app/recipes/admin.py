from django.contrib import admin
from recipes.models import Ingredient, Recipe, RecipeIngredients


class IngredientInline(admin.TabularInline):
    """A class that adds forms for RecipeIngredients."""

    model = RecipeIngredients
    extra = 1  # initial number of forms to add new ingredients


class RecipeAdmin(admin.ModelAdmin):
    """A class to add recipes with forms for new ingredients."""
    inlines = (IngredientInline,)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
