from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class MeasurementType(models.TextChoices):
    GRAM = 'g', 'Gram'
    MILLILITER = 'ml', 'Milliliter'
    POUNDS = 'lbs', 'Pounds'
    OUNCES = 'oz', 'Ounces'
    TEASPOON = 'tsp', 'Teaspoon'
    TABLESPOON = 'tbsp', 'Tablespoon'
    CUP = 'cup', 'Cup'

class CuisineType(models.TextChoices):
    AFRICAN = 'African'
    AMERICAN = 'American'
    ASIAN = 'Asian'
    DESSERT = 'Dessert'
    EUROPEAN = 'European'
    LATIN = 'Latin'
    MIDDLEEASTERN = 'Middle Eastern'
 


class Pantry(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    measurement = models.CharField(
        max_length=4,
        choices=MeasurementType.choices,
        default=MeasurementType.GRAM,
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('pantry_detail', kwargs={'pk': self.id})
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(
        choices=CuisineType.choices,
        default=CuisineType.AFRICAN,
    )
    description = models.TextField(max_length=300)
    pantry = models.ManyToManyField(Pantry)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'recipe_id': self.id})
    
class Instruction(models.Model):
    step = models.PositiveIntegerField()
    instruction = models.TextField(max_length=250)

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        ordering = ['step']

    def __str__(self):
        return f"Step {self.step}: {self.instruction}"