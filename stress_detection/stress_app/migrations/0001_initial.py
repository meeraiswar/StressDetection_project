# Generated by Django 5.1.3 on 2024-11-19 05:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StressData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snoring_rate', models.FloatField()),
                ('respiratory_rate', models.FloatField()),
                ('body_temperature', models.FloatField()),
                ('limb_movement', models.FloatField()),
                ('blood_oxygen', models.FloatField()),
                ('eye_movement', models.FloatField()),
                ('sleep_hours', models.FloatField()),
                ('heart_rate', models.FloatField()),
                ('stress_level', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
