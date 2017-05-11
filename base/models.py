# coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Company(models.Model):
    Code = models.CharField(max_length=20)
    Name = models.CharField(max_length=50)
    PoName = models.CharField(max_length=200, blank=True, null=True)
    ShortName = models.CharField(max_length=20)
    EnShortName = models.CharField(max_length=20, blank=True, null=True)
    Address = models.CharField(max_length=200)
    Tel = models.CharField(max_length=20)
    Fax = models.CharField(max_length=20, blank=True, null=True)
    Email = models.EmailField(blank=True, null=True)
    Web = models.URLField(blank=True, null=True)
    Type = models.CharField(
        max_length=1, choices=(('1', '子公司'), ('2', '分判公司')))

    class Admin:
        list_display = ('Code', 'Name', 'PoName', 'ShortName',
                        'EnShortName', 'Address', 'Tel', 'Fax', 'Email', 'Web', 'Type')

    def __unicode__(self):
        return self.Name

    class Meta(object):
    	ordering = ['Code']
# coding:utf-8