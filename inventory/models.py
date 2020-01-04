from django.db import models
import datetime
from django.utils import timezone

class Item(models.Model):
    def __str__(self):
        return self.name

    WHOLESALE = 'W'
    RETAIL = 'R'
    sale_type_choices = [
        (WHOLESALE, 'Wholesale'),
        (RETAIL, 'Retail'),
    ]
    name = models.CharField('Item Name', max_length = 512)
    description = models.TextField('Item Description')
    date_published = models.DateField('Date Published', auto_now_add=True)
    last_modified = models.DateTimeField('Last Modified', auto_now=True)
    price = models.DecimalField('Price', max_digits=None, decimal_places=2)
    sale_type = models.CharField('Sale Type', choices=sale_type_choices, default=RETAIL)
