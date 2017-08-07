# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname=models.CharField(max_length=20,default='环泰')
    upwd=models.CharField(max_length=40)
    uphone = models.CharField(max_length=11,default='')

