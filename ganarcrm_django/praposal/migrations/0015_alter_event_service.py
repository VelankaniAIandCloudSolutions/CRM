# Generated by Django 4.1.5 on 2023-08-07 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('praposal', '0014_remove_package_group_service_service_package_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='praposal.service'),
        ),
    ]