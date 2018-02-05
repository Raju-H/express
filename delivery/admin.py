from django.contrib import admin
from .models import CarList, DriverName, TripList, TripCost


class CarModelAdmin(admin.ModelAdmin):
    class Meta:
        model = CarList
    list_display = ['__str__', 'addedon']
    list_filter = ['addedon']


admin.site.register(CarList, CarModelAdmin)


class DriverModelAdmin(admin.ModelAdmin):
    class Meta:
        model = DriverName
    list_display = ['__str__', 'addedon']
    list_filter = ['addedon']


admin.site.register(DriverName, DriverModelAdmin)


class TripModelAdmin(admin.ModelAdmin):
    class Meta:
        model = TripList
    list_display = ['__str__', 'trip_no', 'addedon']
    list_filter = ['addedon']


admin.site.register(TripList, TripModelAdmin)


class CostModelAdmin(admin.ModelAdmin):
    class Meta:
        model = TripCost
    list_display = ['__str__', 'addedon']
    list_filter = ['addedon']


admin.site.register(TripCost, CostModelAdmin)
