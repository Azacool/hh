from django.db import models
from django.utils.html import mark_safe

class Content(models.Model):
    contact = models.CharField(max_length=100,blank=False)
    listing = models.TextField()
    image = models.ImageField(default='defaultav.jpg')

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="80" height="80" />' % (self.image))

    image_tag.short_description = 'Image'

    def __str__(self) -> str:
        return self.contact

