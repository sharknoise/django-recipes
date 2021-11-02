from django.db import models


class Ingredient(models.Model):
    name = models.CharField(
        "Название",
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = "recipes"
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class Recipe(models.Model):
    name = models.CharField("Название", max_length=200)
    description = models.TextField(
        "Описание",
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
    """A model for many-to-many relation between Recipe and Ingredient."""

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.PROTECT,
        verbose_name='Ингредиент',
    )
    amount = models.CharField("Количество", max_length=100, blank=True)

    class Meta:
        verbose_name = "Ингредиент рецепта"
        verbose_name_plural = "Ингредиенты рецепта"
