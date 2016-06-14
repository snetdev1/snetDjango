from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User, Group


class party(models.Model):
    name = models.CharField('Party name', max_length=255)
    location = models.CharField('Location', max_length=255)
    description = models.CharField('description', max_length=255)
    start = models.DateTimeField('Start')
    length = models.IntegerField('Length')
    active = models.BooleanField('Active')
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['start']

    def __unicode__(self):
        return u'%s' % (self.name)
