# Generated by Django 4.1.2 on 2024-02-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer_Account', '0006_remove_customeraccount_national_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraccount',
            name='user_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, unique=True),
        ),
    ]