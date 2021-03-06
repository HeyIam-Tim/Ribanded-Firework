from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=200, null=True)
  image = models.ImageField(null=True, blank=True)

  def __str__(self):
    return self.name

  @property
  def imageURL(self):
    try:
      url = self.image.url
    except:
      url = ''
    return url