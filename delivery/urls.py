from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.car_list),
    url(r'^(?P<id>\d+)/$', views.details_report, name='detail'),
    url(r'^pdf/$', views.GeneratePdf.as_view())
]