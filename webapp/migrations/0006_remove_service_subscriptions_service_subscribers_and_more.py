# Generated by Django 4.2.3 on 2023-08-10 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_service_subscriptions_alter_subscription_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='subscriptions',
        ),
        migrations.AddField(
            model_name='service',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='subscribed_services', through='webapp.Subscription', to='webapp.subscriber'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.service'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='subscriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.subscriber'),
        ),
    ]
