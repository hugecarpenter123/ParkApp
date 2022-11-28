from django.db import models

# Create your models here.

from django.db import models
from django.db.models.signals import post_save, pre_save
from django.utils.timezone import datetime

# Create your models here.

class Location(models.Model):
    PAYMENT_CHOICES = [
        ("free", "Free"),
        ("paid", "Paid"),
        ("unknown", "Unknown")
    ]
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    isFree = models.CharField(
        choices=PAYMENT_CHOICES,
        max_length=7,
        default="Unknown"
    )
    address = models.CharField(max_length=100, default="Nie określony")
    plus_code = models.CharField(max_length=100, null=True)



    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    rows = models.IntegerField()
    columns = models.IntegerField()

    def __str__(self):
        return f'{self.location}/{self.name}/{self.spot_set.all().count()}'

    @classmethod
    def post_create(cls, sender, instance, created, *args, **kwargs):
        if created:
            for row in range(1, instance.rows + 1):
                for col in range(1, instance.columns + 1):
                    spot = Spot.objects.create(section=instance,
                                               row=row,
                                               column=col,
                                               status='free')
                    spot.save()
                    print(f"{spot.row}.{spot.column} at {spot.section} - created")

post_save.connect(Section.post_create, sender=Section)

class Spot(models.Model):
    STATUS_CHOICES = [
        ("free", "Free"),
        ("occupied", "Occupied"),
    ]
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    row = models.IntegerField()
    column = models.IntegerField()
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=8,
        default="free"
    )
    # date_updated = models.DateTimeField('date_updated', auto_now=True)

    @classmethod
    def onStatusChange(self, sender, instance, **kwargs):
        if instance.id:
            location = instance.section.location
            print("----------------")
            print(location)
            print("----------------")
            current_status = instance.status
            previous_status = Spot.objects.get(id=instance.id).status
            if previous_status == 'free' and current_status == "occupied":
                Motion.objects.create(location=location)
                print('tutaj będzie counter++')

    def __str__(self):
        return f'{self.section}/{self.row}.{self.column}'

pre_save.connect(Spot.onStatusChange, sender=Spot)

class Motion(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)



