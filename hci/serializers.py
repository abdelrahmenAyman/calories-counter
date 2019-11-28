from rest_framework import serializers

from hci.models import FoodItem


class AddFoodItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodItem
        fields = ('pk', 'name', 'calories_value')

    def validate_calories_value(self, value):
        user_profile = self.context['request'].user.profile
        if user_profile.consumed_calories_today + value > user_profile.allowed_calories_per_day:
            raise serializers.ValidationError('Can not add this item, calory limit for today will be exceeded')
        return value

    def create(self, validated_data):
        user_profile = self.context['request'].user.profile
        user_profile.update_consumed_calories(validated_data['calories_value'])
        validated_data['profile'] = user_profile
        return super().create(validated_data)


class FoodItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodItem
        fields = ('pk', 'name', 'calories_value')
