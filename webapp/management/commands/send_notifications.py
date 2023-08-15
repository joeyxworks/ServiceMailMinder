from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, timedelta
from webapp.models import Service, Subscription
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Sends an email notification for services expiring in 30 days'

    def handle(self, *args, **kwargs):
        services_expiring_soon = Service.objects.filter(expired_on__lte=datetime.now()+timedelta(days=45), notifying=True)
        #print(services_expiring_soon)
        for service in services_expiring_soon:
            subscriptions = Subscription.objects.filter(service=service)
            #print(subscriptions)
            for subscription in subscriptions:
                try:
                    send_mail(
                    'Service Expiration Notification',
                    f'The service {service.service_name} at branch {service.branch} is expiring on {service.expired_on}.',
                    settings.EMAIL_HOST_USER,
                    [subscription.subscriber.email],
                    fail_silently=False,
                    )

                    self.stdout.write(self.style.SUCCESS('Notifications sent successfully!'))
                except Exception as e:
                    # Log the error
                    logger.error(f"Error sending notifications: {e}")
                    # Informative message for failure
                    self.stdout.write(self.style.ERROR('Failed to send notifications.'))
