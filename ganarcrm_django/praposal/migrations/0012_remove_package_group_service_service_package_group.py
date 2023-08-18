# Generated by Django 4.1.5 on 2023-08-04 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('praposal', '0011_alter_package_group_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package_group',
            name='service',
        ),
        migrations.AddField(
            model_name='service',
            name='package_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='praposal.package_group'),
        ),
    ]