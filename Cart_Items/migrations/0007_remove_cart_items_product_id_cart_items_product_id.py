# Generated by Django 4.1.2 on 2024-02-04 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_product_product_video_alter_product_product_image'),
        ('Cart_Items', '0006_alter_cart_items_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_items',
            name='product_id',
        ),
        migrations.AddField(
            model_name='cart_items',
            name='product_id',
            field=models.ManyToManyField(to='Product.product', verbose_name='Product in cart'),
        ),
    ]