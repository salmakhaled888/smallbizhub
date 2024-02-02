# Generated by Django 4.1.2 on 2024-02-02 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order_Details', '0004_alter_order_details_user_id'),
        ('Order_Items', '0002_alter_order_items_deleted_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_items',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Order_Details.order_details', verbose_name='Order ID'),
        ),
    ]