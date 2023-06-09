# Generated by Django 4.1.5 on 2023-04-25 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0010_remove_quote_is_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quotation_status',
            field=models.CharField(blank=True, choices=[('new', 'new'), ('accepted', 'accepted'), ('on_going', 'on_going'), ('completed', 'completed'), ('rejected', 'rejected')], max_length=255),
        ),
    ]
