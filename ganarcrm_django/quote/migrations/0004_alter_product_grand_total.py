# Generated by Django 4.1.5 on 2023-03-29 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0003_product_tax_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='grand_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
