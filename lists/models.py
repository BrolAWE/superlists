from django.conf import settings
from django.db import models
from django.urls import reverse


class List(models.Model):
    '''список'''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        '''получить абсолютный url'''
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    '''элемент списка'''
    text = models.TextField(default='')
    list = models.ForeignKey(List, on_delete=models.CASCADE, default=None)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text
