from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.
class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True, unique=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

class ActiveLinkManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(active=True)

        objects = models.Manager()
        public = ActiveLinkManager()

def __str__(self):
    return self.description
