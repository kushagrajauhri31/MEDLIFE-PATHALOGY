# Generated by Django 4.2.4 on 2023-12-02 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathology', '0003_remove_cart_taxes_remove_cart_total_price_cart_gst_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
