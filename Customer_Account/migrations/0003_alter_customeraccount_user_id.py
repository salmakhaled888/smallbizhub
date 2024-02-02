# Generated by Django 4.1.2 on 2024-02-02 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Customer_Account', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraccount',
            name='user_id',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User ID'),
        ),
    ]
