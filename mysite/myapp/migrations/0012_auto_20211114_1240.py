# Generated by Django 3.0 on 2021-11-14 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0011_studentclassroomlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentclassroomlist',
            name='studentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
