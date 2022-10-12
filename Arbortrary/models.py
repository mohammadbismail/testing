from django.db import models
from django.forms import DateField
from log_reg_app.models import *
import re


class TreeManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['species']) < 5:
            errors["species"] = "Species must be at least 5 characters."
        if len(postData['location']) < 3:
            errors["location"] = "Location must be at least 2 characters."
        if len(postData['reason']) > 50:
            errors["reason"] = "Reason exceeded 50 characters!"
        return errors


class Tree(models.Model):

    objects = TreeManager()

    species = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    reason = models.TextField()
    date_planted = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='trees',
                             on_delete=models.CASCADE)
