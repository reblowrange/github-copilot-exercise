"""
populate_db.py - Script to populate the Octofit Tracker database with test data.

Usage:
    python manage.py shell < populate_db.py
"""

from octofit_tracker.models import User, Activity, Team
from django.contrib.auth.models import User as DjangoUser
from django.utils import timezone

# Create test users
users = [
    {'username': 'alice', 'email': 'alice@example.com', 'password': 'testpass'},
    {'username': 'bob', 'email': 'bob@example.com', 'password': 'testpass'},
    {'username': 'carol', 'email': 'carol@example.com', 'password': 'testpass'},
]
for u in users:
    user, created = DjangoUser.objects.get_or_create(username=u['username'], defaults={'email': u['email']})
    if created:
        user.set_password(u['password'])
        user.save()

# Create test teams
team1, _ = Team.objects.get_or_create(name='Team Alpha')
team2, _ = Team.objects.get_or_create(name='Team Beta')

# Assign users to teams
team1.members.add(DjangoUser.objects.get(username='alice'))
team1.members.add(DjangoUser.objects.get(username='bob'))
team2.members.add(DjangoUser.objects.get(username='carol'))

# Create test activities
activities = [
    {'user': 'alice', 'type': 'Running', 'duration': 30, 'distance': 5.0},
    {'user': 'bob', 'type': 'Cycling', 'duration': 45, 'distance': 15.0},
    {'user': 'carol', 'type': 'Swimming', 'duration': 60, 'distance': 2.0},
]
for a in activities:
    Activity.objects.create(
        user=DjangoUser.objects.get(username=a['user']),
        activity_type=a['type'],
        duration=a['duration'],
        distance=a['distance'],
        date=timezone.now()
    )

print('Test data populated successfully.')
