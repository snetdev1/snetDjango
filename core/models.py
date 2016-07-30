from __future__ import unicode_literals

from django.db import models

#from django.contrib.auth.models import User, Group


class cms (models.Model):

    description = models.CharField('description', max_length=255)
    content = models.TextField('content')

    def __unicode__(self):
        return '%s %s' % (self.id, self.description)

