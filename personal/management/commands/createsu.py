from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="jaspindersingh83").exists():
            User.objects.create_superuser("jaspindersingh83", "jaspindersingh83@gmail.com", "Bawamano@83")
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))