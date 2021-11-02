from django.test import TestCase
from django.urls import reverse

from recipes.models import Recipe, Ingredient


class RecipeFilterTest(TestCase):
    def setUp(self):
        self.ingredient_1 = Ingredient.objects.create(name="test_ingredient")
        Recipe.objects.create(
            name="test_recipe_1", description="test_description_1"
        )
        Recipe.objects.create(
            name="test_recipe_2", description="test_description_2"
        )
        self.test_recipe_3 = Recipe.objects.create(
            name="test_recipe_3", description="test_description_3"
        )
        self.test_recipe_3.ingredients.set(
            Ingredient.objects.filter(name="test_ingredient")
        )

    def test_ingredient_filter(self):
        response = self.client.get(
            reverse("recipes_list"), {"ingredients": self.ingredient_1.id}
        )
        self.assertQuerysetEqual(
            response.context["object_list"],
            Recipe.objects.filter(ingredients=self.ingredient_1),
            ordered=False,
        )

    def test_name_filter(self):
        response = self.client.get(
            reverse("recipes_list"), {"name": "_3"}
        )
        self.assertQuerysetEqual(
            response.context["object_list"],
            Recipe.objects.filter(name="test_recipe_3"),
            ordered=False,
        )
