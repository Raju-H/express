from django.shortcuts import render, get_object_or_404
from .models import TripCost, CarList, TripList
from django.db.models import Sum

from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        instance = CarList.objects.all()
        data = {
            'instance': instance
        }
        pdf = render_to_pdf('index.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


def car_list(request):
    queryset = CarList.objects.all()
    context = {
        'title': 'Welcome | All Car',
        'queryset': queryset,
    }
    return render(request, 'index.html', context)


def details_report(request, id):
    instance = get_object_or_404(TripCost, id=id)

    trip_cost_obj = TripCost.objects.get(id=id)

    trip_list_earn = TripList.objects.filter(trip_no=trip_cost_obj).aggregate(Sum('trip_earn'))

    context = {
        'title': 'Welcome | Report',
        'instance': instance,
        'total_earn': trip_list_earn,
    }
    return render(request, 'details.html', context)
