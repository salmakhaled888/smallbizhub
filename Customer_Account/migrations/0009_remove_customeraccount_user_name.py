# Generated by Django 4.1.2 on 2024-02-03 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer_Account', '0008_customeraccount_address_line1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeraccount',
            name='user_name',
        ),
    ]
