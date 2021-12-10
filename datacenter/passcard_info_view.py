from datetime import datetime, timedelta

import pytz
from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from django_bank_security.settings import TIME_ZONE


def get_visit_duration(start_visit, end_visit):
    start_visit = localtime(start_visit)
    if not end_visit:
        end_visit = localtime(datetime.now())
    else:
        end_visit = localtime(end_visit)

    duration = end_visit - start_visit
    print(duration.seconds)

    if duration > timedelta(minutes=60):
        return {'duration': duration, 'is_strange': True}
    else:
        return {'duration': duration, 'is_strange': False}


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard_id=passcard.pk)
    this_passcard_visits = []
    for visit in passcard_visits:
        visit_serialized = {
            'entered_at': visit.entered_at
        }
        visit_serialized.update(get_visit_duration(visit.entered_at, visit.leaved_at))
        this_passcard_visits.append(visit_serialized)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
