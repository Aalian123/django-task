import pytz
from django.core.management.base import BaseCommand

from Elearning_platform.models import CronJob


class Command(BaseCommand):
    help = 'Converts pst to utc'

    def handle(self, *args, **kwargs):
        start = 0
        end = 10
        # import pdb
        # pdb.set_trace()
        # times = CronJob.objects.all()[start:end]
        # for c in times:
        #     print(c.time)
        #     pst = pytz.timezone('America/Los_Angeles')
        #     pst_time = c.time.astimezone(pst)
        #     local_time = tzlocal.get_localzone()
        #     # c.time.clear()
        #     c.time = c.time.replace(tzinfo=pytz.utc).astimezone(local_time)
        #     c.save()
        for start in range(end):
            time_zone = CronJob.objects.get(name=start)

            pst = pytz.timezone('America/Los_Angeles')
            pst_time = time_zone.time.astimezone(pst)
            # CronJob.objects.update(time=F(pst_time))

            # utc = timezone.utc
            # utc_time = pst_time.astimezone(utc)

            # Update the record with the UTC time
            time_zone.time = pst_time
            time_zone.save()
            print(time_zone.time)
        start = end
        end += 10
        if end == 100:
            start = 0
            end = 10
