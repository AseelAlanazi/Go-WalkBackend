from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
#----------------------------
from .models import Goal,ProgressHistory,Place,FavoritePlace,ReviewAndComments
from .serializers import  GoalSerializer,ProgressHistorySerializer,PlaceSerializer ,FavoritePlaceSerializer,ReviewAndCommentsSerializer
# Create your views here.

class GoalListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
       goal, created = Goal.objects.get_or_create(user=request.user, defaults={'goal': 10000, 'current_progress': 0})
       serializer = GoalSerializer(goal)
       return Response(serializer.data,status=200)
    def patch(self, request):
        goal = Goal.objects.get(user=request.user)
        serializer = GoalSerializer(goal, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            previous_progress = goal.current_progress
            ProgressHistory.objects.create(goal=goal, progress=serializer.validated_data.get('current_progress', previous_progress) )
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
class HistoryListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        history = ProgressHistory.objects.filter(goal__user=request.user)
        serializer = ProgressHistorySerializer(history, many=True)
        return Response(serializer.data, status=200)

class PlaceListView(APIView):
    permission_classes = [AllowAny]
    
    def get(self,request):
      places = Place.objects.all()
      serializer = PlaceSerializer(places,many=True)
      return Response(serializer.data, status=200)
    
class PlaceDetailView(APIView):
    permission_classes = [AllowAny]
    
    def get_object(self, pk):
        return get_object_or_404(Place, pk=pk)
    
    def get(self, request, pk):
        place = self.get_object(pk)
        serializer = PlaceSerializer(place)
        return Response(serializer.data, status=200)
    
class FavoritePlaceView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        favorite = FavoritePlace.objects.filter(user=request.user)
        serializer = FavoritePlaceSerializer(favorite,many=True)
        return Response(serializer.data,status=200)
    def post(self,request):
         serializer = FavoritePlaceSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save(user=request.user) 
            return Response(serializer.data, status=201)
         return Response(serializer.errors, status=400)
    
class FavoritePlaceDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        return get_object_or_404(FavoritePlace, pk=pk)
    def get(self, request, pk):
        favorite = self.get_object(pk)
        serializer = FavoritePlaceSerializer(favorite)
        return Response(serializer.data, status=200)
    def delete(self, request, pk):
        favorite = self.get_object(pk)
        favorite.delete()
        return Response(status=204)
    def patch(self, request, pk):
        favorite = self.get_object(pk)
        serializer = FavoritePlaceSerializer(favorite, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
class ReviewAndCommentsListView(APIView):
    permission_classes = [AllowAny]
    
    def get(self,request,place_id):
      places = ReviewAndComments.objects.filter(place=place_id)
      serializer = ReviewAndCommentsSerializer(places,many=True,context={'request': request})
      return Response(serializer.data, status=200)
    def post(self,request,place_id):
         serializer = ReviewAndCommentsSerializer(data=request.data,context={'request': request})
         if serializer.is_valid():
            serializer.save(user=request.user, place_id=place_id) 
            return Response(serializer.data, status=201)
         return Response(serializer.errors, status=400)
    
class CommentByUser(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self,place_id,pk):
        return get_object_or_404(ReviewAndComments,place_id=place_id,pk=pk)
    def get(self, request,place_id,pk):
        comment = self.get_object(place_id,pk)
        serializer = ReviewAndCommentsSerializer(comment,context={'request': request})
        return Response(serializer.data, status=200)
    def delete(self, request,place_id,pk):
        comment = self.get_object(place_id, pk)
        if comment.user == request.user:
          comment.delete()
          return Response(status=204)
        return Response({"message": "Not your Comment!"},status=403)
    def patch(self, request,place_id,pk):
        comment = self.get_object(place_id,pk)
        if comment.user == request.user:
         serializer = ReviewAndCommentsSerializer(comment, data=request.data,context={'request': request})
         if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
         return Response(serializer.errors, status=400)
        return Response({"message": "Not your Comment!"},status=403)





    
        
            

        
        

        
    
    

class SignUpView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            validate_password(password)
        except ValidationError as err:
            return Response({'error': err.messages}, status=400)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        tokens = RefreshToken.for_user(user)
        return Response(
            {
                'refresh': str(tokens),
                'access': str(tokens.access_token)
            },
            status=201
        )
