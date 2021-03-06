"""
Models from template on genmymodel, with updates
"""
from django.db import models
import datetime

# Create your models here.



class Caregiver(models.Model):
    """
    to get the goals, use caregiver.goal_set
    to get the patients, use caregiver.patient_set
    to get the actions, use caregiver.action_set
    """
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
    def __unicode__(self):
        return self.name



class Patient(models.Model):
    """
    to get goals, use patient.goal_set
    """
    name = models.CharField(max_length=100)
    caregiver = models.ManyToManyField(Caregiver)
    photo = models.ImageField(upload_to='gk/static/gk/img')
    age = models.IntegerField()
    info = models.TextField()
    def __unicode__(self):
        return self.name


class Goal(models.Model):
    """
    to get the status updates, use goal.status_update_set
    """
    name = models.CharField(max_length=100)
    caregivers = models.ManyToManyField(Caregiver)
    patient = models.ForeignKey(Patient)
    notes = models.TextField()
    active = models.BooleanField()
    data_type = models.IntegerField()
    def __unicode__(self):
        return self.name



class StatusUpdate(models.Model):
    goal = models.ForeignKey(Goal)
    pub_time = models.DateTimeField()
    data_value = models.IntegerField()
    reporting_caregiver = models.ForeignKey(Caregiver)
    status = models.TextField()
    def __unicode__(self):
        return self.status


class Action(models.Model):
    goal = models.ForeignKey(Goal)
    completed = models.BooleanField()
    name = models.CharField(max_length=100)
    caregiver = models.ForeignKey(Caregiver)
    deadline = models.DateField()
    def __unicode__(self):
        return self.name
    
