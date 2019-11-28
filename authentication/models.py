from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class ProfileManager(models.Manager):
    """
    The purpose of having this custom manager, is to override the behaviour of .create() to
    create related user field too while creating the profile instance.
    """

    def create(self, email=None, password=None, first_name=None, last_name=None, **obj_data):
        user = User(email=email, username=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()

        obj_data['user'] = user
        return super().create(**obj_data)


class Profile(models.Model):

    objects = ProfileManager()

    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')
    consumed_calories = models.IntegerField(default=0)
    allowed_calories_per_day = models.IntegerField(default=2500)

    @property
    def consumed_calories_today(self):
        """Returns the value of calories added by user today"""
        pass
