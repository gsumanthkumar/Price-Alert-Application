from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save

# Create your models here.
alert_choices = (
    ('created','created'),
    ('deleted','deleted'),
    ('triggered','triggered')
    )



class alert(models.Model):
    name = models.CharField(max_length=60)
    threshold = models.PositiveBigIntegerField(default=0)
    description = models.TextField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(choices=alert_choices,default='created',max_length=15)



    def __str__(self):
        return self.name
    
    def apply_alerts(self):
        if self.threshold == 20000:
            self.status = 'triggered'
        