# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class DeviceInfo(models.Model):
    dtype=models.CharField(max_length=12)
    dname=models.CharField(max_length=16,default='环泰设备')
    dmac=models.CharField(max_length=40)
    dbrand = models.CharField(max_length=20,default='')
    gcontrolcode = models.CharField(max_length=10, default='')
    ggateway = models.ForeignKey('sc_gateway.GatewayInfo')
