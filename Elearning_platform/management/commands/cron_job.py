import pytz
from django.core.management.base import BaseCommand
from django.utils import timezone

from Elearning_platform.models import CronJob


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        pst = pytz.timezone('America/Los_Angeles')
        for i in range(100):
            timezone.activate(pst)
            CronJob.objects.create(name=i, time=timezone.now().astimezone(pst))
            print(timezone.now().astimezone(pst))
