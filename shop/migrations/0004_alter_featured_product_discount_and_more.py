# Generated by Django 4.2.8 on 2024-01-16 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_featured_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featured_product',
            name='discount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='featured_product',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
