# Generated by Django 4.1.2 on 2024-02-02 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seller_Account', '0006_selleraccount_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selleraccount',
            name='business_field',
        ),
        migrations.RemoveField(
            model_name='selleraccount',
            name='business_name',
        ),
    ]
