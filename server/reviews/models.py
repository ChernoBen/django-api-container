from django.contrib.auth.models import User
from django.db import models

class Reviews(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    review = models.TextField()
    date_review = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
