# Generated by Django 4.1.5 on 2023-07-28 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('praposal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='default_item',
            name='default_package',
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name', models.CharField(blank=True, max_length=255, null=True)),
                ('option_time', models.CharField(blank=True, max_length=255, null=True)),
                ('default_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='praposal.default_package')),
            ],
        ),
        migrations.AddField(
            model_name='default_item',
            name='option',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='default_items', to='praposal.option'),
            preserve_default=False,
        ),
    ]
