from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone


# Create your models here.

    
class Stock(models.Model):
    def __str__(self):
        return self.stock_text
    



