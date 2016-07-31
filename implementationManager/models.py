from django.db import models
from django.contrib.auth.models import User, Group


class project(models.Model):
    name = models.CharField('Project name', max_length=255)
    active = models.BooleanField('Active')
    location = models.CharField('Location', max_length=255)
    apiurl = models.CharField('API', max_length=255)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return u'%s' % (self.name)


class projectUser(models.Model):
    project = models.ForeignKey(project)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['user']

    def __unicode__(self):
        return u'%s %s' % (self.project, self.user)

class projectGroup(models.Model):
    project = models.ForeignKey(project)
    group = models.ForeignKey(Group)
    def __unicode__(self):
        return u'%s %s' % (self.project, self.group)