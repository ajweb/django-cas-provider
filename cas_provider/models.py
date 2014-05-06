from django.db import models
from django.conf import settings

class ServiceTicket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    service = models.URLField()
    ticket = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s (%s) - %s" % (self.user.username, self.service, self.created)
        
class LoginTicket(models.Model):
    ticket = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s - %s" % (self.ticket, self.created)