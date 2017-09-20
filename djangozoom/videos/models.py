# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Webinar(models.Model):

    meeting = models.CharField(max_length=30)
