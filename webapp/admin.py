from django.contrib import admin
from .models import Service, Subscriber, Subscription
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User

class UserAdmin(DefaultUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name'),
        }),
    )

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'branch', 'expired_on', 'notifying')  # Fields you want to display in the list view
    search_fields = ('service_name', 'branch')  # Fields you want to be searchable
    list_filter = ('branch', 'notifying')

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'subscriber')  # Fields you want to display in the list view
    search_fields = ('service__service_name', 'subscriber__first_name', 'subscriber__last_name')  # Fields you want to be searchable
    list_filter = ('service', 'subscriber')  # Fields you want to use as filters

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Subscription, SubscriptionAdmin)