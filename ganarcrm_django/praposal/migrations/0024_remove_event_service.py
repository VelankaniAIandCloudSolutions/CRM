# Generated by Django 4.1.5 on 2023-08-08 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('praposal', '0023_function_alter_event_service_function_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='service',
        ),
    ]
