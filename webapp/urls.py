from django.urls import path
from .views import (
    ServiceListView,
    ServiceCreateView,
    ServiceUpdateView,
    ServiceDeleteView,
    #ServiceBulkDeleteView,
    ServiceBulkActionView,
    SubscriberCreateView,
    SubscriberDeleteView,
    ServiceDetailView,
)

urlpatterns = [
    path('', ServiceListView.as_view(), name='service-list'),
    path('service/add/', ServiceCreateView.as_view(), name='service-create'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('service/<int:pk>/edit/', ServiceUpdateView.as_view(), name='service-update'),
    path('service/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service-delete'),
    path('subscriber/add/', SubscriberCreateView.as_view(), name='subscriber-create'),
    path('subscriber/<int:pk>/delete/', SubscriberDeleteView.as_view(), name='subscriber-delete'),
    path('service/bulk_action/', ServiceBulkActionView.as_view(), name='service-bulk-action'),
    #path('service/bulk_delete/', ServiceBulkDeleteView.as_view(), name='service-bulk-delete'),
]

# urlpatterns = [
#     path('', ServiceListView.as_view(), name='service_list'),
#     path('')
#     #path('send-test-email/', SendTestEmailView.as_view())
# ]


