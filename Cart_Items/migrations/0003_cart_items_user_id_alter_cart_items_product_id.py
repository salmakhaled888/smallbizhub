# Generated by Django 4.1.2 on 2024-02-02 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer_Account', '0003_alter_customeraccount_user_id'),
        ('Product', '0001_initial'),
        ('Cart_Items', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_items',
            name='user_id',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='Customer_Account.customeraccount', verbose_name='Customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart_items',
            name='product_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Product.product', verbose_name='Product in cart'),
        ),
    ]