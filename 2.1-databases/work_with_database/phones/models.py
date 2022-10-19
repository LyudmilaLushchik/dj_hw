from django.db import models as m
from django.core.validators import MinValueValidator


class Phone(m.Model):    
    name = m.CharField(max_length=100, null=False)
    price = m.IntegerField(validators=[MinValueValidator(1)])
    image = m.TextField()
    release_date = m.DateField()
    lte_exists = m.BooleanField()
    slug = m.SlugField(max_length = 200)