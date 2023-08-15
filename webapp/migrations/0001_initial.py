# Generated by Django 4.2.3 on 2023-07-14 05:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('expired_on', models.DateField()),
                ('notifying', models.BooleanField(default=False)),
                ('subscribers', models.ManyToManyField(related_name='services', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]