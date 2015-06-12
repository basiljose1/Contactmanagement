from django.db import models

# Create your models here.

class Name(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    #group_code  = models.ForeignKey(Group)
    def __str__(self):              # __unicode__ on Python 2
        return self.first_name+' '+self.last_name


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
    def __str__(self):              # __unicode__ on Python 2
        return str(self.group_name)


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
