# Generated by Django 4.1.2 on 2024-02-01 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=100)),
                ('last_name', models.CharField(default=None, max_length=100)),
                ('telephone', models.PositiveIntegerField(default=None)),
                ('created_at', models.DateField(default=None)),
                ('modified_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
