from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from pymongo import MongoClient

# Sample data for users, teams, activities, leaderboard, workouts
USERS = [
    {"email": "ironman@marvel.com", "username": "ironman", "team": "marvel"},
    {"email": "captainamerica@marvel.com", "username": "captainamerica", "team": "marvel"},
    {"email": "batman@dc.com", "username": "batman", "team": "dc"},
    {"email": "superman@dc.com", "username": "superman", "team": "dc"},
]

TEAMS = [
    {"name": "marvel", "members": ["ironman", "captainamerica"]},
    {"name": "dc", "members": ["batman", "superman"]},
]

ACTIVITIES = [
    {"user": "ironman", "activity": "run", "distance": 5},
    {"user": "batman", "activity": "cycle", "distance": 10},
]

LEADERBOARD = [
    {"user": "ironman", "points": 100},
    {"user": "batman", "points": 90},
]

WORKOUTS = [
    {"name": "Pushups", "difficulty": "easy"},
    {"name": "Sprints", "difficulty": "hard"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Insert test data
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        # Ensure unique index on email
        db.users.create_index("email", unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
