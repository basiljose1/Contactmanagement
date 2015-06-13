from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericRelation


# Create your models here.

GENDER_CHOICES = (
	('male', _('Male')),
	('female', _('Female')),
	('other', _('Other'))
)

class Name(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(_('gender'),max_length=200,choices=GENDER_CHOICES,default='male')
    organization = models.CharField(max_length=200)
    def __str__(self):              # __unicode__ on Python 2
        return self.email
        #return self.first_name+self.last_name
    def __iter__(self):
        return [ self.first_name,  
                 self.last_name, 
                 self.email, 
                 self.dob, 
                 self.gender, 
                 self.organization] 


class Contract(models.Model):
    contract = models.ForeignKey(Name)
    from_date = models.DateTimeField('From date')
    to_date = models.DateTimeField('To date')
    list_size = models.IntegerField(default=1)
    total_email = models.IntegerField(default=1)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.contract)


class Group(models.Model):
    group_code = models.CharField(max_length=16, unique=True)
    group_name = models.CharField(max_length=200)
    Group_des = models.TextField(max_length=200)
    people = models.ManyToManyField(Name, verbose_name='Names', blank=True,
		null=True)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.group_name)


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

