# Generated by Django 4.1.5 on 2023-04-27 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('client', '0006_alter_file_client_alter_file_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='team.team'),
        ),
    ]
