# Generated by Django 4.1.5 on 2023-08-04 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praposal', '0010_alter_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package_group',
            name='name',
            field=models.CharField(blank=True, choices=[('food', 'food'), ('beverages', 'beverages'), ('alcohol', 'alcohol')], max_length=255, null=True),
        ),
    ]
