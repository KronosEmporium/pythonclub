from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingtitle = models.CharField( max_length = 255 )
    meetingdate = models.DateField()
    meetingtime = models.TimeField()
    location = models.CharField( max_length = 255 )
    agenda = models.TextField( null = True, blank = True )

    def __str__(self):
        return self.meetingtitle
        
    class Meta():
        db_table = 'meeting'
        verbose_name_plural = 'meetings'
    
class MeetingMinutes(models.Model):
    meeting = models.ForeignKey( Meeting, on_delete = models.DO_NOTHING )
    attendance = models.ManyToManyField( User )
    minutes = models.TextField( null = True, blank = False )

    def __str__(self):
        return self.minutes

    class Meta():
        db_table = 'minutes'

class Resource(models.Model):
    resourcename = models.CharField( max_length = 255 )
    resourcetype = models.CharField( max_length = 255 )
    resourceURL = models.URLField( null = True, blank = True )
    dateentered = models.DateField()
    user = models.ForeignKey( User, on_delete = models.DO_NOTHING )
    description = models.TextField( null = True, blank = True )

    def __str__(self):
        return self.resourcename
    
    class Meta():
        db_table = 'resource'
        verbose_name_plural = 'resources'

class Event(models.Model):
    eventtitle = models.CharField( max_length = 255 )
    location = models.CharField( max_length = 255 )
    eventdate = models.DateField()
    eventtime = models.TimeField()
    postedby = models.ForeignKey( User, on_delete = models.DO_NOTHING )
    description = models.TextField( null = True, blank = True )
    
    def __str__(self):
        return self.eventtitle
    
    class Meta():
        db_table = 'event'
        verbose_name_plural = 'events'