from django.db import models
from django.core.urlresolvers import reverse


class CarList(models.Model):
    addedon = models.DateTimeField(auto_now=True)
    car_number = models.CharField(max_length=128)

    def __str__(self):
        return str(self.car_number)

    class Meta:
        ordering = ['-addedon']


class DriverName(models.Model):
    addedon = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=256)
    mobile_number = models.CharField(max_length=14)
    address = models.CharField(max_length=256)
    nid = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class TripCost(models.Model):
    addedon = models.DateTimeField(auto_now=True)
    car_no = models.ForeignKey(CarList, on_delete=models.CASCADE)
    driver_name = models.ForeignKey(DriverName, on_delete=models.CASCADE)
    trip_number = models.CharField(max_length=256)
    dieasel_liter = models.CharField(max_length=256)
    dieasel_amount = models.CharField(max_length=256)
    feri_bridge = models.CharField(max_length=256)
    police_labour = models.CharField(max_length=256)
    chada = models.CharField(max_length=256)
    khoraki = models.CharField(max_length=256)
    car_parts = models.CharField(max_length=256)
    others = models.CharField(max_length=256)
    trip_earn_money = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return str(self.trip_number)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})

    class Meta:
        ordering = ['-addedon']

    def results(self):
        a = float(self.dieasel_liter) * float(self.dieasel_amount)
        b = float(self.others)+float(self.feri_bridge)+float(self.police_labour)+float(self.chada)+float(self.khoraki)+float(self.car_parts)+float(self.trip_earn_money)
        c = a + b
        return float(c)


class TripList(models.Model):
    trip_no = models.ForeignKey(TripCost, on_delete=models.CASCADE)
    addedon = models.DateTimeField(auto_now=True)
    trip_description = models.CharField(max_length=256)
    trip_earn = models.CharField(max_length=256)

    def __str__(self):
        return self.trip_description

    def trip_earn_total(self):
        return float(self.trip_earn)