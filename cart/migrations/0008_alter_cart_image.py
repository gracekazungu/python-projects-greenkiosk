# Generated by Django 3.2.12 on 2023-08-06 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_cart_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]