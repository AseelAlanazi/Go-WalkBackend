from rest_framework import serializers
from .models import Goal,Place ,FavoritePlace,ReviewAndComments ,ProgressHistory

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}} 

class ProgressHistorySerializer(serializers.ModelSerializer):
    updated_at = serializers.DateTimeField(format="%Y-%m-%d",read_only=True)
    class Meta:
        model = ProgressHistory
        fields = '__all__'
        
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
class FavoritePlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritePlace
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}} 

class ReviewAndCommentsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    adding_at = serializers.DateTimeField(format="%Y-%m-%d",read_only=True)
    class Meta:
        model = ReviewAndComments
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True},'place': {'read_only': True}} 
    def get_username(self, obj):
        return obj.user.username
    def get_is_owner(self, obj):
        return self.context['request'].user == obj.user
       
