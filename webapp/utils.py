from django.core.mail import send_mail

def notify_subscribers(email_list, message):
    send_mail(
        'Service Expiration Notification',  # subject
        message,  # message
        'DCMC_IT_Network@eimglobal.com',  # from email
        email_list,  # recipient list
        fail_silently=False,
    )
