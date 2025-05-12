from django.db import models
from django.contrib.auth.models import User  

# Create your models here.
class Goal(models.Model):
    goal = models.IntegerField()
    current_progress = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
                return f'{self.user.username} - Goal : {self.goal}'
        
class ProgressHistory(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='history')
    progress = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta :
               ordering = ['-updated_at'] 
    
class Place(models.Model):
        name = models.CharField(max_length=255)
        description = models.TextField(max_length=1000)
        location = models.CharField(max_length=255)
        img = models.CharField(max_length=255)
        
        def __str__(self):
                return f'{self.name} in {self.location}'

class FavoritePlace(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        name = models.CharField(max_length=255)
        location = models.CharField(max_length=255)
        img = models.CharField(max_length=255,null=True, blank=True)

class ReviewAndComments(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        place = models.ForeignKey(Place,on_delete=models.CASCADE)
        comment = models.TextField(max_length=1000)
        rating = models.IntegerField()
        adding_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
         return f'{self.user.username} review on {self.place.name}'
 
        class Meta :
               ordering = ['-adding_at'] 



