# Generated by Django 4.1.2 on 2024-02-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller_Account', '0002_alter_selleraccount_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='selleraccount',
            name='national_id',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True),
        ),
    ]
