# -*- coding: utf-8 -*-
from .models import DeviceInfo
from rest_framework import serializers

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInfo
        fields = ('id', 'dtype', 'dname', 'dmac','dbrand','gcontrolcode','ggateway')
