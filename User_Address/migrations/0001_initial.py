# Generated by Django 4.1.2 on 2024-02-01 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(default=None, max_length=40)),
                ('address_line2', models.CharField(default=None, max_length=40)),
                ('city', models.CharField(default=None, max_length=40)),
                ('postal_code', models.CharField(default=None, max_length=40)),
                ('country', models.CharField(default=None, max_length=40)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user_address')),
            ],
        ),
    ]