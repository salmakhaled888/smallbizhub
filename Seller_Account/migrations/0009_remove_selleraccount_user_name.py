# Generated by Django 4.1.2 on 2024-02-03 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seller_Account', '0008_selleraccount_address_line1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selleraccount',
            name='user_name',
        ),
    ]
