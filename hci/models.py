from django.db import models

from authentication.models import Profile


class FoodItem(models.Model):

    profile = models.ForeignKey(to=Profile, on_delete=models.CASCADE, related_name='food_items')

    name = models.CharField(max_length=150)
    calories_value = models.IntegerField()
