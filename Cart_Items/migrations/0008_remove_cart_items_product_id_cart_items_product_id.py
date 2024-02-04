# Generated by Django 4.1.2 on 2024-02-04 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_product_product_video_alter_product_product_image'),
        ('Cart_Items', '0007_remove_cart_items_product_id_cart_items_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_items',
            name='product_id',
        ),
        migrations.AddField(
            model_name='cart_items',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.product', verbose_name='Product in cart'),
        ),
    ]