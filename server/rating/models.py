from django.db import models
from django.contrib.auth.models import User


class Rating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    comment = models.TextField(null=True,blank=True)
    rate = models.DecimalField(max_digits=1,decimal_places=1)
    date_rating = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username