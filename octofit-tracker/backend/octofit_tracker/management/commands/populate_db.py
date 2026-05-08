from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Create Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team='marvel'),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team='marvel'),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team='dc'),
            User.objects.create(name='Batman', email='batman@dc.com', team='dc'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='run', duration=30, date='2024-01-01')
        Activity.objects.create(user=users[1], activity_type='cycle', duration=45, date='2024-01-02')
        Activity.objects.create(user=users[2], activity_type='swim', duration=60, date='2024-01-03')
        Activity.objects.create(user=users[3], activity_type='yoga', duration=20, date='2024-01-04')

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Squats', description='Do 30 squats', difficulty='medium')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
