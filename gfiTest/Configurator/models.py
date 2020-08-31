# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from mptt.models import MPTTModel
from treewidget.fields import TreeForeignKey

# Create your models here.

class Equipment(MPTTModel):
    name = models.CharField(max_length=200)
    layout = models.TextField(blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name="children")

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Customer(models.Model):
    name = models.CharField(max_length=200)
    ip = models.GenericIPAddressField()
    hostname = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    equipment = TreeForeignKey(Equipment, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        print(timezone.now())
        return super(Customer, self).save(*args, **kwargs)

    def get_layout(self):
        return self.equipment.layout
