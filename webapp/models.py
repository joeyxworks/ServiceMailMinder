from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Service(models.Model):
    service_name = models.CharField(max_length=255)
    branch = models.CharField(max_length=255, null=True, blank=True)  # New field
    expired_on = models.DateField()
    subscriptions = models.ManyToManyField('Subscriber', through='Subscription', related_name='subscribed_services')
    #subscribers = models.ManyToManyField('Subscriber', related_name='subscribed_services', blank=True)
    #subscribers = models.ManyToManyField('Subscriber', through='Subscription', related_name='subscribed_services', blank=True)
    notifying = models.BooleanField(default=True)
    #branch = models.CharField(max_length=255)
    service_provider = models.CharField(max_length=255, null=True, blank=True)  # New field
    sales_email = models.EmailField(null=True, blank=True)    

    def __str__(self):
        return self.service_name

class Subscriber(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

# class Subscription(models.Model):
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
#     # ... any additional fields ...

#     class Meta:
#         unique_together = ('service', 'subscriber')


class Subscription(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_subscriptions')
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE, related_name='subscriptions')

    class Meta:
        unique_together = ('service', 'subscriber')

    
        
