from django.urls import path


from .views import GoalListView,HistoryListView,SignUpView,PlaceListView,FavoritePlaceView,FavoritePlaceDetailView,ReviewAndCommentsListView,PlaceDetailView,CommentByUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('goal/',GoalListView.as_view(),name='goal'),
    path('goal/history/',HistoryListView.as_view(),name='goal-history'),
    path('places/',PlaceListView.as_view(), name='places'),
    path('places/<int:pk>/',PlaceDetailView.as_view(), name='places-Detail'),
    path('places/<int:place_id>/comments/',ReviewAndCommentsListView.as_view(), name='comments'),
    path('places/<int:place_id>/comments/<int:pk>/',CommentByUser.as_view(), name='comments-detail'),
    path('favorite-place/',FavoritePlaceView.as_view(), name='Favorite-Place'),
    path('favorite-place/<int:pk>/',FavoritePlaceDetailView.as_view(), name='Favorite-Place-Detail'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name='signup')
]