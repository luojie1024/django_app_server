# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class GatewayInfo(models.Model):
    gname=models.CharField(max_length=16,default='环泰网关')
    gmac=models.CharField(max_length=40)
    gpasscode = models.CharField(max_length=24,default='')
    gdid = models.CharField(max_length=16, default='')
    guser = models.ForeignKey('sc_user.UserInfo')
