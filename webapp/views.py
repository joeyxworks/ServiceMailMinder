from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Service, Subscriber
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views import View
from django.conf import settings
from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from django.urls import reverse_lazy

# Create your views here.
class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'
    context_object_name = 'service'

class ServiceListView(ListView):
    model = Service
    template_name = 'service_list.html'
    #template_name = 'home.html'
    context_object_name = 'services'

class ServiceCreateView(CreateView):
    model = Service
    fields = ['service_name', 'branch', 'expired_on', 'notifying', 'service_provider', 'sales_email']
    template_name = 'service_form.html'  # to be created in templates folder
    
    def get_success_url(self):
        return reverse_lazy('service-list')

class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['service_name', 'branch', 'expired_on', 'notifying', 'service_provider', 'sales_email']
    template_name = 'service_form.html'  # same form as create
    
    def get_success_url(self):
        return reverse_lazy('service-list')

class ServiceBulkActionView(View):
    def post(self, request, *args, **kwargs):
        service_ids = request.POST.getlist('service_ids')
        action = request.POST.get('action')  # This will get the value of the clicked button

        if action == 'delete':
            Service.objects.filter(id__in=service_ids).delete()
        elif action == 'notify':
            services_to_notify = Service.objects.filter(id__in=service_ids)
            for service in services_to_notify:
                service.notifying = not service.notifying
                service.save()

        return redirect('service-list')

# class ServiceBulkNotifyView(View):
#     def post(self, request, *args, **kwargs):
#         service_ids = request.POST.getlist('service_ids')
#         services_to_notify = Service.objects.filter(id__in=service_ids)
#         for service in services_to_notify:
#             service.notifying = not service.notifying
#             service.save()
#         return redirect('service-list')


class ServiceDeleteView(DeleteView):
    model = Service
    fields = ['service_name', 'branch', 'expired_on', 'notifying', 'service_provider', 'sales_email']
    template_name = 'service_form.html'  # same form as create

# class ServiceBulkDeleteView(View):
#     def post(self, request, *args, **kwargs):
#         service_ids = request.POST.getlist('service_ids')  # 'service_ids' should match the checkbox name
#         Service.objects.filter(id__in=service_ids).delete()
#         return redirect('service-list')

class SubscriberCreateView(CreateView):
    model = Subscriber
    fields = ['name', 'email']
    template_name = 'subscriber_form.html'  # to be created in templates folder

class SubscriberDeleteView(DeleteView):
    model = Subscriber
    template_name = 'subscriber_confirm_delete.html'  # to be created in templates folder
    success_url = '/'  # to redirect after deleting

# class SendTestEmailView(View):
#     def get(self, request, *args, **kwargs):
#         send_mail(
#             'Notification Center',
#             'This is a test email from IT Notification Center.',
#             'DCMC_IT_Network@eimglobal.com',
#             ['joey.chen@cn.eimglobal.com'],
#             fail_silently=False,
#         )
#         return HttpResponse('Email has been sent successfully')


