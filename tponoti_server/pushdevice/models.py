# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Devices(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=400)

