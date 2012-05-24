# -*-coding: utf-8-*-
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(verbose_name=u'ФИО', max_length=50)
    birthday = models.DateField(verbose_name=u'Дата рождения')
    number = models.CharField(verbose_name=u'№ зачётки', max_length=20)
    group = models.ForeignKey('Group', 
                              verbose_name=u'Группа:',
                              null=True, 
                              blank=True, 
                              on_delete=models.SET_NULL,
                              related_name=('Group'))
    
    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.number)
    
class Group(models.Model):
    title = models.CharField(verbose_name=u'Название', max_length=10)
    elder = models.ForeignKey('Student', 
                              verbose_name=u'Староста:',
                              null=True, 
                              blank=True, 
                              on_delete=models.SET_NULL,
                              related_name=(u'Student'))
    
    def __unicode__(self):
        return u'%s' % (self.title)