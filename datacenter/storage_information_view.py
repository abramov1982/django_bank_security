from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Visit
from .passcard_info_view import get_visit_duration


def storage_information_view(request):
    visitors_in_storage = Visit.objects.filter(leaved_at__isnull='NULL')
    non_closed_visits = []
    for visitor in visitors_in_storage:
        visitor_serialize = {'who_entered': visitor.passcard.owner_name,
                             'entered_at': localtime(visitor.entered_at),
                             'duration': str(get_visit_duration(visitor.entered_at)['duration']).split(".")[0]}
        non_closed_visits.append(visitor_serialize)
    context = {'non_closed_visits': non_closed_visits}
    return render(request, 'storage_information.html', context)
