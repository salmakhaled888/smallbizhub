# Generated by Django 4.1.2 on 2024-02-01 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Seller_Account', '0001_initial'),
        ('Product_Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default=None, max_length=100)),
                ('product_image', models.ImageField(upload_to='Product Images')),
                ('product_description', models.TextField(default=None, max_length=1000)),
                ('SKU', models.CharField(default=None, max_length=12)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=3, default=None, max_digits=10000000)),
                ('created_at', models.DateField(default=None)),
                ('modified_at', models.DateField(auto_now=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product_Category.product_categories', verbose_name='category')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller_Account.selleraccount', verbose_name='seller')),
            ],
        ),
    ]