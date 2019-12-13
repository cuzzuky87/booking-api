
from django.db import models
from django.contrib.auth import get_user_model

class Reservation(models.Model):
    user = models.ForeignKey(
       get_user_model(),
       on_delete=models.CASCADE 
    )
    title = models.CharField(max_length=100)
    statrt_at = models.DateTimeField()
    end_at  = models.DateTimeField()
    
