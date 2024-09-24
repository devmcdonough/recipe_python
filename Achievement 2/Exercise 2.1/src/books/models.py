from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=120)
    genre_choices = (
        ('cl', 'Classic'),
        ('ro', 'Romantic'),
        ('co', 'Comic'),
        ('fa', 'Fantasy'),
        ('ho', 'Horror'),
        ('ed', 'Educational')
    )
    genre = models.CharField(max_length=12, 
                             choices=genre_choices,
                             default='cl')
    book_type_choices = (
        ('hc', 'Hardcover'),
        ('eb', 'E-Book'),
        ('ab', 'Audiobook')
    )
    book_type = models.CharField(max_length=12,
                                 choices=book_type_choices,
                                 default='hc')
    price = models.FloatField(help_text='in $USD')
    author_name = models.CharField(max_length=120)
    pic = models.ImageField(upload_to='books', default='no_picture.png')

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse ('books:detail', kwargs={'pk': self.pk})

