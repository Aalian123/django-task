from .models import CronJob
from django.utils import timezone
import pytz


def update_to_utc():
    end = 10
    for start in range(end):
        time_zone = CronJob.objects.get(name=start)
        pst = pytz.timezone('America/Los_Angeles')
        pst_time = time_zone.time.astimezone(pst)

        utc = timezone.utc
        utc_time = pst_time.astimezone(utc)

        time_zone.time = utc_time
        time_zone.save()
