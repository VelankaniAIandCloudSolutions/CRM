# Generated by Django 4.1.5 on 2023-03-29 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quote', '0007_remove_product_description_remove_product_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
