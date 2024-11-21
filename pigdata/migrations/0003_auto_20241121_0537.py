# Generated by Django 3.0.3 on 2024-11-21 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pigdata', '0002_general_identification_and_parentage_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='health_parameter_vaccination',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='general_identification_and_parentage',
            unique_together={('user', 'animal_id')},
        ),
    ]
