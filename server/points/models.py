from django.db import models
from attractions.models import Attractions
from reviews.models import Reviews
from rating.models import Rating
from address.models import Address

class Points(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attractions,default=None)
    reviews = models.ManyToManyField(Reviews,default=None)
    rate = models.ManyToManyField(Rating,default=None)
    address = models.ForeignKey(Address,on_delete=models.CASCADE,default=None,null=True,blank=True)

    def __str__(self):
        return self.name


