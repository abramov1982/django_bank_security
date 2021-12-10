from datetime import datetime

import pytz
from django.utils.timezone import localtime

from datacenter.models import Visit
from django.shortcuts import render

from django_bank_security.settings import TIME_ZONE


def storage_information_view(request):
    visitors_in_storage = Visit.objects.filter(leaved_at__isnull='NULL')
    non_closed_visits = []
    for visitor in visitors_in_storage:
        visitor_serialize = {'who_entered': visitor.passcard.owner_name,
                             'entered_at': localtime(visitor.entered_at),
                             'duration': str(datetime.now(pytz.timezone(TIME_ZONE))-localtime(visitor.entered_at)).split(".")[0]}
        non_closed_visits.append(visitor_serialize)
    context = {'non_closed_visits': non_closed_visits}
    return render(request, 'storage_information.html', context)
