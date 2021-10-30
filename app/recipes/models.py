from django.db import models


class Ingredient(models.Model):
    name = models.CharField(
        "Название",
        max_length=100,
        unique=True,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = "recipes"
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
    )

    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredients',
        blank=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = "recipes"
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
