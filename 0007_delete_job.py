# Generated by Django 5.0.3 on 2024-04-10 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pathology', '0006_report_report_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Job',
        ),
    ]
