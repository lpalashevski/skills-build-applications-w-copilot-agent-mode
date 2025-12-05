"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from pymongo import MongoClient
from django.http import JsonResponse

# Helper to get MongoDB collection
def get_collection(name):
    client = MongoClient('mongodb://localhost:27017')
    db = client['octofit_db']
    return db[name]

# Serializers (dummy, as we use MongoDB directly)
class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    team = serializers.CharField()

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField()
    members = serializers.ListField(child=serializers.CharField())

class ActivitySerializer(serializers.Serializer):
    user = serializers.CharField()
    activity = serializers.CharField()
    distance = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    user = serializers.CharField()
    points = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField()
    difficulty = serializers.CharField()

# ViewSets
import os

def get_api_base_url():
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        return f"https://{codespace_name}-8000.app.github.dev/api/"
    return "http://localhost:8000/api/"

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = list(get_collection('users').find({}, {'_id': 0}))
        # Add API base URL to response for demonstration
        return JsonResponse({"api_base_url": get_api_base_url(), "users": users}, safe=False)

class TeamViewSet(viewsets.ViewSet):
    def list(self, request):
        teams = list(get_collection('teams').find({}, {'_id': 0}))
        return JsonResponse({"api_base_url": get_api_base_url(), "teams": teams}, safe=False)

class ActivityViewSet(viewsets.ViewSet):
    def list(self, request):
        activities = list(get_collection('activities').find({}, {'_id': 0}))
        return JsonResponse({"api_base_url": get_api_base_url(), "activities": activities}, safe=False)

class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        leaderboard = list(get_collection('leaderboard').find({}, {'_id': 0}))
        return JsonResponse({"api_base_url": get_api_base_url(), "leaderboard": leaderboard}, safe=False)

class WorkoutViewSet(viewsets.ViewSet):
    def list(self, request):
        workouts = list(get_collection('workouts').find({}, {'_id': 0}))
        return JsonResponse({"api_base_url": get_api_base_url(), "workouts": workouts}, safe=False)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutViewSet, basename='workout')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
